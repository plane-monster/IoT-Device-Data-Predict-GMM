from pyomo.environ import *
import numpy as np
# this version mec3 is for changed the b_i and b_s to let them have different upperbounds in different time slots and devices
# only this difference, compared with mec2
# V=list(range(10))
# T=list(range(10))
# Ebatt_Cap = {t: 2000 for t in range(len(T))}
# Dbatt_Cap = {(t, i): 1000 for t in range(len(T)) for i in range(len(V))}
def MILP(V,M,N,T,Dstore_Cap,Estore_Cap,Dbatt_Cap,Ebatt_Cap,CPU_Cap,E_i,B_i,E_s,B_s,F_i,Len_slot,Energy_percpu,Input_size,Workload,Error_coe,Error_var,Error_thre,Channel_g,Compu_VMcap,Channel_band,Noise_pow,Appro_ratio,VM_consu,Rho):
    #code of pyomo MILP
    model = ConcreteModel(name="(MEC)")
    model.x = Var(V, within=Binary) #$x_i$
    model.y = Var(V, within=Binary)  # $y_i$
    model.z = Var(T, V, M ,within=Binary) #$z_{im}^{t}$
    model.f = Var(T, V, N ,within=Binary)  #$f_{in}^{t}$
    model.w_i = Var(T, V,bounds = (0,Dstore_Cap))  #$w_{i}^{t}$
    model.w_s = Var(T, bounds=(0, Estore_Cap))  #$w_{s}^{t}$
    model.b_i = Var(T, V, bounds=lambda model, t,i: (0, Dbatt_Cap[t,i]))  # $b_{i}^{t}$
    model.b_s = Var(T, bounds=lambda model, t: (0, Ebatt_Cap[t]))  # $b_{s}^{t}$
    model.phi = Var(T, V, bounds=(0, CPU_Cap)) #$\phi_{i}^{t}$

    # Constraint(1)
    def Energy_arrival_device_rule(model,t,i):
        return model.w_i[t,i]-E_i[t,i] <= 0

    model.Energy_arrival_device = Constraint(T, V, rule=Energy_arrival_device_rule)

    # Constraint(2)
    # HTJ: B_i可以直接设置成整数，就是说所有device的battery容量一样。11
    def Battery_device_rule(model,t,i):
        return model.b_i[t,i]+model.w_i[t,i]-B_i[i] <= 0

    model.Battery_device = Constraint(T, V, rule=Battery_device_rule)

    # Constraint(3)
    def Energy_arrival_server_rule(model,t):
        return model.w_s[t]-E_s[t] <= 0

    model.Energy_arrival_server = Constraint(T, rule=Energy_arrival_server_rule)

    # Constraint(4)
    def Battery_server_rule(model,t):
        return model.b_s[t]+model.w_s[t]-B_s <= 0

    model.Battery_server = Constraint(T, rule=Battery_server_rule)

    # Constraint(5)
    # HTJ: \tau表示一个slot的长度，一般设为1 11
    def CPU_time_slot_rule(model,t,i):
        return model.phi[t,i]-F_i[i]*Len_slot <= 0

    model.CPU_time_slot = Constraint(T, V, rule=CPU_time_slot_rule)

    # Constraint(6)
    def CPU_energy_rule(model,t,i):
        return model.phi[t,i]-(model.b_i[t,i]/Energy_percpu)<= 0

    model.CPU_energy = Constraint(T, V, rule=CPU_energy_rule)

   # Constraint(7)
    def CPU_computing_rule(model,i):
        return model.x[i]*Input_size[i]*Workload[i]-sum(model.phi[t,i] for t in T) <= 0

    model.CPU_computing = Constraint(V, rule=CPU_computing_rule)

    # Constraint(8)
    def Device_computing_mode_rule(model, i):
        return model.y[i]-model.x[i] <= 0

    model.Device_computing_mode = Constraint(V, rule=Device_computing_mode_rule)

    # Constraint(9)
    # （9）中的Error_coe和Error_var可以直接设成常数，对所有值都一样11
    def Approximate_error_bound_rule(model):
        return sum(model.y[i]*Error_coe[i]*Error_var[i] for i in V)-Error_thre <= 0

    model.Approximate_error_bound = Constraint(rule=Approximate_error_bound_rule)

    # Constraint(11)
    def Channel_device_bound_rule(model,t,n):
        return sum(model.f[t,i,n] for i in V)-1 <= 0

    model.Channel_device_bound = Constraint(T,N, rule=Channel_device_bound_rule)

    # Constraint(12)
    def Device_channel_bound_rule(model,i):
        return sum(model.f[t,i,n]  for t in T for n in N)-1 +model.x[i]<= 0

    model.Device_channel_bound = Constraint(V, rule=Device_channel_bound_rule)

    # Constraint(13)
    def VM_upload_rule(model,t,m):
        return sum(model.z[t,i,m] for i in V)-1<= 0

    model.VM_upload = Constraint(T,M, rule=VM_upload_rule)

    # HTJ 这个错了
    # def VM_upload_slot_rule(model,t,i):
    #     return sum(model.z[t,i,m] for m in M)-sum(model.f[t,i,n] for t in T for n in N)+sum(model.f[t,i,n] for n in N) <= 0
    #
    # model.VM_upload_slot = Constraint(T,M, rule=VM_upload_slot_rule)

    # Constraint(14)
    def VM_upload_slot_rule(model,t,i):
        if t == 0:
            for m in M:
                return model.z[t,i,m]  == 0
        else:
            return sum(model.z[t,i,m] for m in M)-sum(model.f[t,i,n] for t in T[0:t] for n in N) <= 0

    model.VM_upload_slot = Constraint(T,V, rule=VM_upload_slot_rule)

    # Constraint(15)
    # HTJ 看（15）大于等于，这个错了11
    def VM_upload_task_rule(model):
        return sum((1-model.x[i])*Input_size[i]*Workload[i] for i in V)-sum(model.z[t,i,m]*Compu_VMcap[m] for i in V for t in T for m in M)<= 0

    model.VM_upload_task = Constraint(rule=VM_upload_task_rule)


    Tran_pow=np.zeros((len(T),len(V),len(N))) #$P_{i}^{t}$
    for t in range(len(T)):
        for i in range(len(V)):
            for n in range(len(N)):
                Tran_pow[t, i, n] = 1e-3*pow(10,((pow(2, Input_size[i] / Channel_band) - 1)* Noise_pow-30)/10) / Channel_g[t, i, n]


    # model.Device_up = Var(T, V, bounds=(0, Up_Cap))  # $\lamda_{i}^{Ut}$
    # Constraint(17)
    # HTJ Device_up是什么，注意（17）和（18）可以合并。
    # def Device_upload_task_rule(model,t,i):
    #     return sum(model.f[t,i,n]*Tran_pow[t,i,n]*Len_slot/Input_size[i] for n in N)-model.Device_up[t,i] == 0
    #
    # model.Device_upload_task = Constraint(T,V,rule=Device_upload_task_rule)

    # Constraint(17)-(18)
    # def Energy_upload_task_rule(model,t,i):
    #     return sum(model.f[t,i,n]*Tran_pow[t,i,n]*Len_slot/Input_size[i] for n in N)-model.b_i[t,i]<= 0
    #
    # model.Energy_upload_task = Constraint(T,V,rule=Energy_upload_task_rule)


    # model.Energy_local = Var(V, bounds=(0, Energy_Caplocal))  # $\lamda_{i}^{L}$
    # Constraint(20)
    # HTJ 20 和21可以合并。
    # def Energy_device_upload_task_rule(model,i):
    #     return model.y[i]*Input_size[i]*Workload[i]*Energy_percpu+(model.x[i]-model.y[i])*Appro_ratio*Input_size[i]*Workload[i]*Energy_percpu-model.Energy_local[i] == 0
    #
    # model.Energy_device_upload_task = Constraint(V,rule=Energy_device_upload_task_rule)


    # Constraint(20)-(21)
    def Energy_device_harvest_rule(model,i):
        return model.y[i]*Input_size[i]*Workload[i]*Energy_percpu*Appro_ratio+(model.x[i]-model.y[i])*Input_size[i]*Workload[i]*Energy_percpu-sum(model.w_i[t,i] for t in T) <= 0

    model.Energy_device_harvest = Constraint(V,rule = Energy_device_harvest_rule)


    # model.Energy_server = Var(T, bounds=(0, Energys_Captotal))  # $\lamda_{s}^{t}$
    # Constraint(22)
    # HTJ 22和23合并，这个公式没有意义,==约束建模时容易出问题。
    # def Energy_total_server_rule(model, t):
    #     if  t==0:
    #         return model.Energy_server[t] == 0
    #     else:
    #         return sum(model.z[t, i, m] * VM_consu for m in M for i in V) + sum(model.f[t, i, n] * Input_size[i] * Rho for i in V for n in N) - model.Energy_server[t] == 0
    #
    #
    # model.Energy_total_server = Constraint(T, rule=Energy_total_server_rule)


    # Constraint(22)-(23)
    # HTJ Energy_server表示能耗。
    def Energy_server_harvest_rule(model, t):
        if t == 0:
            return model.b_s[t] == 0
        else:
            return model.b_s[t] - model.b_s[t - 1] - model.w_s[t - 1] + sum(model.z[t, i, m] * VM_consu for m in M for i in V) + sum(model.f[t, i, n] * Input_size[i] * Rho for i in V for n in N) == 0

    model.Energy_server_harvest = Constraint(T, rule=Energy_server_harvest_rule)


    # Constraint(24)
    # HTJ 参考公式，改成<=0，Pyomo一般用<=011
    def Task_all_excution_rule(model, i):

        return -model.x[i] - sum(model.z[t,i,m] for t in T for m in M) + 1 <= 0

    model.Task_all_excution = Constraint(V, rule=Task_all_excution_rule)



    #####Object
    def obj_rule(model):
        return sum(model.z[t, i, m] * VM_consu for m in M for i in V for t in T) + sum(model.f[t, i, n] * Input_size[i] * Rho for i in V for n in N for t in T)  + sum(model.f[t,i,n]*Tran_pow[t,i,n]*Len_slot/Input_size[i] for n in N for t in T for i in V) + sum(model.y[i]*Input_size[i]*Workload[i]*Energy_percpu*Appro_ratio+(model.x[i]-model.y[i])*Input_size[i]*Workload[i]*Energy_percpu for i in V)
    model.obj = Objective(rule=obj_rule, sense=minimize)

    #  Solve the MILP
    opt = SolverFactory('gurobi', solver_io='python')
    results = opt.solve(model) # solves and updates instance
    Max_min_Opt = value(model.obj)

    #record local excuting in device i
    Device_localexcute=[0]*len(V)
    for i in range(len(V)):
        Device_localexcute[i]=model.x[i].value

    #record approximate mode in device i
    Device_approximate=[0]*len(V)
    for i in range(len(V)):
        Device_approximate[i]=model.y[i].value

    #record channel allocation to device i in time slot t
    Channel_allocation=np.zeros((len(T),len(V),len(N)))
    for t in range(len(T)):
        for i in range(len(V)):
            for n in range(len(N)):
                Channel_allocation[t,i,n]=model.f[t,i,n].value

    #record VM assignment by device i in time slot t
    VM_assignment=np.zeros((len(T),len(V),len(M)))
    for t in range(len(T)):
        for i in range(len(V)):
            for m in range(len(M)):
                VM_assignment[t,i,m]=model.z[t,i,m].value

    # record the energy consumption of the sever at the set of time slots (T)
    Energy_server = np.zeros(len(T))
    for t in range(len(T)):
        Energy_server[t] = sum(value(model.z[t, i, m]) * VM_consu for m in M for i in V) + sum(value(model.f[t, i, n]) * Input_size[i] * Rho for i in V for n in N)

    # record the energy consumption of the devices at the set of time slots (T)
    Energy_device = np.zeros((len(T),len(V)))
    for t in range(len(T)):
        for i in range(len(V)):
            Energy_device[t,i] = abs(sum(value(model.f[t,i,n])*Tran_pow[t,i,n]*Len_slot/Input_size[i] for n in N)+value(model.y[i])*Input_size[i]*Workload[i]*Energy_percpu*Appro_ratio+(value(model.x[i])-value(model.y[i]))*Input_size[i]*Workload[i]*Energy_percpu)






    # model.pprint()
    # model.x.pprint()
    # model.y.pprint()
    # model.w_i.pprint()
    # model.z.pprint()
    # model.f.pprint()
    # model.w_i.pprint()
    # model.phi.pprint()
    # model.b_i.pprint()
    # print(E_i)
    # print(E_s)
    # print(F_i)
    # print(Input_size)
    # print(Workload)
    # print(Channel_g)
    # print(Device_localexcute)
    # print(Device_approximate)
    # print(sum(Device_localexcute))
    # print(sum(Device_approximate))
    # print(sum(Channel_allocation))
    # print(sum(VM_assignment))
    # return [Max_min_Opt, Energy_server, Energy_device]
    # return [Device_localexcute,Device_approximate]
    return [Max_min_Opt,Device_localexcute,Device_approximate,VM_assignment,Channel_allocation]

    # return Max_min_Opt,Device_localexcute,Device_approximate,Channel_allocation,VM_assignment

