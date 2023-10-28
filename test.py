import Solar
import NetworkBasic
import MEC_FOR_RHC
import numpy as np
import random
import GMM
import mec3
import random_decision

# #number of devices
# num_v=[8,12,16,18,20,24]
# #number of experiment
# num = 5
# #temp value for optimal and random solution and matrix for all of them
# opt = 0
# ran = 0
# sol = np.zeros((2,len(num_v)))
# for z in num_v:
# #Size of the time window
#     opt = 0
#     ran = 0
#     K = 7
#     # Device Parameters
#     V = list(range(z))
#     M = list(range(10))
#     N = list(range(10))
#     T = list(range(20))
#     Dstore_Cap = 1000
#     Estore_Cap = 2000
#     Ebatt_Cap = np.array([2000] * len(T))
#     Dbatt_Cap = np.array([[1000] * len(V)] * len(T))
#     #devie cpu capacity
#     CPU_Cap = 5e+8#(in cycle)
#     B_i = [1e+3] * len(V)
#     B_s = 2e+3
#     # Computationla capacity of device
#     F_i = [2e+9] * len(V)#(in cycle/s)
#     Len_slot = 1
#     Energy_percpu = 2.5e-12#(in J/cycle)
#     Error_coe = [0.005] * len(V)
#     Error_var = [1.2] * len(V)
#     Error_thre = 0.02
#     Compu_VMcap = [1e+10] * len(M)#（in cycle)
#     Channel_band = 1e+7#(in Hz)
#     Noise_pow = -87#(dBM)
#     Appro_ratio = 0.5
#     VM_consu = 1.5#(in J)
#     Rho = 1.5e-7#(J/bit)
#     # Fixed input data size and workload
#     Input_size = [1.5e+5] * len(V)#(in bit)
#     Workload = [1e+3] * len(V)#(in cycle/bit)
#     # Generate all time slot data for solar energy arrival for nodes and server, channel gain value
#     E_ih = Solar.Solar_Value(len(V), T, 900)  # 3000-17000
#     E_sh = Solar.Solar_Value(1, T, 900)
#     Channel_gh = NetworkBasic.Calculate_Channel_Gain(len(T), len(V), len(N))
#     # Compute the optimal solution of all the time slots apart from the history time slots
#     E_i0 = E_ih[K:]
#     E_s0 = E_sh[K:]
#     Channel_g0 = Channel_gh[K:, :, :]
#     #predict the future K data of solar energy of devices,server and chanel gain(prediction phase)
#     future_Es_all = GMM.GMMs(E_sh[0:K],len(E_i0))
#     future_Ei_all = GMM.GMMi(E_ih[0:K],len(E_i0))
#     future_g_all = GMM.GMMg(Channel_gh[0:K],len(E_i0))
#     for j in range(num):
#         [Max_min_Opt0,X0,Y0,Z0,F0] = mec3.MILP(V, M, N, T[0:(len(T) - K)], Dstore_Cap, Estore_Cap,
#                                                                    Dbatt_Cap[K:], Ebatt_Cap[K:], CPU_Cap, E_i0, B_i,
#                                                                    E_s0,
#                                                                    B_s, F_i, Len_slot,
#                                                                    Energy_percpu, Input_size, Workload, Error_coe,
#                                                                    Error_var, Error_thre, Channel_g0, Compu_VMcap,
#                                                                    Channel_band,
#                                                                    Noise_pow, Appro_ratio, VM_consu, Rho)
#         opt = opt + Max_min_Opt0
#
#         #random strategy
#         [X_random, Y_random, Z_random, F_random] = random_decision.randomize_XYZF(X0,Y0,Z0,F0)
#
#         # compute the energy consumption of random strategy
#         energy_device_local_random = 0
#         for i in range(len(X_random)):
#             energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]
#         energy_upload_random = 0
#         # Tran_pow
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
#         energy_server_random = sum(Z_random[t, i, m] * VM_consu for m in M for i in V for t in list(range(len(T[K:])))) + sum(F_random[t, i, n] * Input_size[i] * Rho for i in V for n in N for t in list(range(len(T[K:]))))
#         energy_upload_device = sum(F_random[t, i, n] * Tran_pow[t, i, n] * Len_slot / Input_size[i] for n in N for t in list(range(len(T[K:])))for i in V)
#         energy_random = energy_server_random + energy_upload_device + energy_device_local_random
#         ran = ran + energy_random
#     sol[0,num_v.index(z)] = opt/num
#     sol[1,num_v.index(z)] = ran/num
#     print(sol)



# #number of CHANNELS
# num_n=[8,12,16,18,20,24]
# #number of experiment
# num = 5
# #temp value for optimal and random solution and matrix for all of them
# opt = 0
# ran = 0
# sol = np.zeros((2,len(num_n)))
# for z in num_n:
# #Size of the time window
#     K = 7
#     opt = 0
#     ran = 0
#     # Device Parameters
#     V = list(range(10))
#     M = list(range(10))
#     N = list(range(z))
#     T = list(range(20))
#     Dstore_Cap = 1000
#     Estore_Cap = 2000
#     Ebatt_Cap = np.array([2000] * len(T))
#     Dbatt_Cap = np.array([[1000] * len(V)] * len(T))
#     #devie cpu capacity
#     CPU_Cap = 5e+8#(in cycle)
#     B_i = [1e+3] * len(V)
#     B_s = 2e+3
#     # Computationla capacity of device
#     F_i = [2e+9] * len(V)#(in cycle/s)
#     Len_slot = 1
#     Energy_percpu = 2.5e-12#(in J/cycle)
#     Error_coe = [0.005] * len(V)
#     Error_var = [1.2] * len(V)
#     Error_thre = 0.02
#     Compu_VMcap = [1e+10] * len(M)#（in cycle)
#     Channel_band = 1e+7#(in Hz)
#     Noise_pow = -87#(dBM)
#     Appro_ratio = 0.5
#     VM_consu = 1.5#(in J)
#     Rho = 1.5e-7#(J/bit)
#     # Fixed input data size and workload
#     Input_size = [1.5e+5] * len(V)#(in bit)
#     Workload = [1e+3] * len(V)#(in cycle/bit)
#     # Generate all time slot data for solar energy arrival for nodes and server, channel gain value
#     E_ih = Solar.Solar_Value(len(V), T, 900)  # 3000-17000
#     E_sh = Solar.Solar_Value(1, T, 900)
#     Channel_gh = NetworkBasic.Calculate_Channel_Gain(len(T), len(V), len(N))
#     # Compute the optimal solution of all the time slots apart from the history time slots
#     E_i0 = E_ih[K:]
#     E_s0 = E_sh[K:]
#     Channel_g0 = Channel_gh[K:, :, :]
#     #predict the future K data of solar energy of devices,server and chanel gain(prediction phase)
#     future_Es_all = GMM.GMMs(E_sh[0:K],len(E_i0))
#     future_Ei_all = GMM.GMMi(E_ih[0:K],len(E_i0))
#     future_g_all = GMM.GMMg(Channel_gh[0:K],len(E_i0))
#     for j in range(num):
#         [Max_min_Opt0,X0,Y0,Z0,F0] = mec3.MILP(V, M, N, T[0:(len(T) - K)], Dstore_Cap, Estore_Cap,
#                                                                    Dbatt_Cap[K:], Ebatt_Cap[K:], CPU_Cap, E_i0, B_i,
#                                                                    E_s0,
#                                                                    B_s, F_i, Len_slot,
#                                                                    Energy_percpu, Input_size, Workload, Error_coe,
#                                                                    Error_var, Error_thre, Channel_g0, Compu_VMcap,
#                                                                    Channel_band,
#                                                                    Noise_pow, Appro_ratio, VM_consu, Rho)
#         opt = opt + Max_min_Opt0
#
#         #random strategy
#         [X_random, Y_random, Z_random, F_random] = random_decision.randomize_XYZF(X0,Y0,Z0,F0)
#
#         # compute the energy consumption of random strategy
#         energy_device_local_random = 0
#         for i in range(len(X_random)):
#             if i == 0 or i == 1:
#                 energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]*random.choice([0,Appro_ratio])
#             else:
#                 energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]
#
#         energy_upload_random = 0
#         # Tran_pow
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
#         energy_server_random = sum(Z_random[t, i, m] * VM_consu for m in M for i in V for t in list(range(len(T[K:])))) + sum(F_random[t, i, n] * Input_size[i] * Rho for i in V for n in N for t in list(range(len(T[K:]))))
#         energy_upload_device = sum(F_random[t, i, n] * Tran_pow[t, i, n] * Len_slot / Input_size[i] for n in N for t in list(range(len(T[K:])))for i in V)
#         energy_random = energy_server_random + energy_upload_device + energy_device_local_random
#         ran = ran + energy_random
#     sol[0,num_n.index(z)] = opt/num
#     sol[1,num_n.index(z)] = ran/num
#     print(sol)


# #ETA approximation ratio
# eta=[0.1,0.3,0.5,0.7,0.9]
# #number of experiment
# num = 5
# #temp value for optimal and random solution and matrix for all of them
# opt = 0
# ran = 0
# sol = np.zeros((2,len(eta)))
# for z in eta:
# #Size of the time window
#     opt = 0
#     ran = 0
#     K = 7
# # Device Parameters
#     V = list(range(10))
#     M = list(range(10))
#     N = list(range(10))
#     T = list(range(20))
#     Dstore_Cap = 1000
#     Estore_Cap = 2000
#     Ebatt_Cap = np.array([2000] * len(T))
#     Dbatt_Cap = np.array([[1000] * len(V)] * len(T))
#     #devie cpu capacity
#     CPU_Cap = 5e+8#(in cycle)
#     B_i = [1e+3] * len(V)
#     B_s = 2e+3
#     # Computationla capacity of device
#     F_i = [2e+9] * len(V)#(in cycle/s)
#     Len_slot = 1
#     Energy_percpu = 2.5e-12#(in J/cycle)
#     Error_coe = [0.005] * len(V)
#     Error_var = [1.2] * len(V)
#     Error_thre = 0.02
#     Compu_VMcap = [1e+10] * len(M)#（in cycle)
#     Channel_band = 1e+7#(in Hz)
#     Noise_pow = -87#(dBM)
#     Appro_ratio = z
#     VM_consu = 1.5#(in J)
#     Rho = 1.5e-7#(J/bit)
#     # Fixed input data size and workload
#     Input_size = [1.5e+5] * len(V)#(in bit)
#     Workload = [1e+3] * len(V)#(in cycle/bit)
#     # Generate all time slot data for solar energy arrival for nodes and server, channel gain value
#     E_ih = Solar.Solar_Value(len(V), T, 900)  # 3000-17000
#     E_sh = Solar.Solar_Value(1, T, 900)
#     Channel_gh = NetworkBasic.Calculate_Channel_Gain(len(T), len(V), len(N))
#     # Compute the optimal solution of all the time slots apart from the history time slots
#     E_i0 = E_ih[K:]
#     E_s0 = E_sh[K:]
#     Channel_g0 = Channel_gh[K:, :, :]
#     #predict the future K data of solar energy of devices,server and chanel gain(prediction phase)
#     future_Es_all = GMM.GMMs(E_sh[0:K],len(E_i0))
#     future_Ei_all = GMM.GMMi(E_ih[0:K],len(E_i0))
#     future_g_all = GMM.GMMg(Channel_gh[0:K],len(E_i0))
#     for j in range(num):
#         [Max_min_Opt0,X0,Y0,Z0,F0] = mec3.MILP(V, M, N, T[0:(len(T) - K)], Dstore_Cap, Estore_Cap,
#                                                                    Dbatt_Cap[K:], Ebatt_Cap[K:], CPU_Cap, E_i0, B_i,
#                                                                    E_s0,
#                                                                    B_s, F_i, Len_slot,
#                                                                    Energy_percpu, Input_size, Workload, Error_coe,
#                                                                    Error_var, Error_thre, Channel_g0, Compu_VMcap,
#                                                                    Channel_band,
#                                                                    Noise_pow, Appro_ratio, VM_consu, Rho)
#         opt = opt + Max_min_Opt0
#
#         #random strategy
#         [X_random, Y_random, Z_random, F_random] = random_decision.randomize_XYZF(X0,Y0,Z0,F0)
#
#         # compute the energy consumption of random strategy
#         energy_device_local_random = 0
#         for i in range(len(X_random)):
#             if i==0 or i==1 or i==3:
#                 energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]
#             else:
#                 energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu *  X_random[i]*random.choice([1,Appro_ratio])
#         energy_upload_random = 0
#         # Tran_pow
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = 1e-3*pow(10,((pow(2, Input_size[i] / Channel_band) - 1)* Noise_pow-30)/10) / Channel_g0[t, i, n]
#         energy_server_random = sum(Z_random[t, i, m] * VM_consu for m in M for i in V for t in list(range(len(T[K:])))) + sum(F_random[t, i, n] * Input_size[i] * Rho for i in V for n in N for t in list(range(len(T[K:]))))
#         energy_upload_device = sum(F_random[t, i, n] * Tran_pow[t, i, n] * Len_slot / Input_size[i] for n in N for t in list(range(len(T[K:])))for i in V)
#         energy_random = energy_server_random + energy_upload_device + energy_device_local_random
#         ran = ran + energy_random
#     sol[0,eta.index(z)] = opt/num
#     sol[1,eta.index(z)] = ran/num
#     print(sol)
#



# #data size
# num_d=[2e+5,6e+5,10e+5,12e+5]
# #number of experiment
# num = 5
# #temp value for optimal and random solution and matrix for all of them
# opt = 0
# ran = 0
# sol = np.zeros((2,len(num_d)))
# for z in num_d:
# #Size of the time window
#     K = 7
#     opt = 0
#     ran = 0
#     # Device Parameters
#     V = list(range(10))
#     M = list(range(10))
#     N = list(range(10))
#     T = list(range(20))
#     Dstore_Cap = 1000
#     Estore_Cap = 2000
#     Ebatt_Cap = np.array([2000] * len(T))
#     Dbatt_Cap = np.array([[1000] * len(V)] * len(T))
#     #devie cpu capacity
#     CPU_Cap = 5e+8#(in cycle)
#     B_i = [1e+3] * len(V)
#     B_s = 2e+3
#     # Computationla capacity of device
#     F_i = [2e+9] * len(V)#(in cycle/s)
#     Len_slot = 1
#     Energy_percpu = 2.5e-12#(in J/cycle)
#     Error_coe = [0.005] * len(V)
#     Error_var = [1.2] * len(V)
#     Error_thre = 0.02
#     Compu_VMcap = [1e+10] * len(M)#（in cycle)
#     Channel_band = 1e+7#(in Hz)
#     Noise_pow = -87#(dBM)
#     Appro_ratio = 0.5
#     VM_consu = 1.5#(in J)
#     Rho = 1.5e-7#(J/bit)
#     # Fixed input data size and workload
#     Input_size = [z] * len(V)#(in bit)
#     Workload = [1e+3] * len(V)#(in cycle/bit)
#     # Generate all time slot data for solar energy arrival for nodes and server, channel gain value
#     E_ih = Solar.Solar_Value(len(V), T, 900)  # 3000-17000
#     E_sh = Solar.Solar_Value(1, T, 900)
#     Channel_gh = NetworkBasic.Calculate_Channel_Gain(len(T), len(V), len(N))
#     # Compute the optimal solution of all the time slots apart from the history time slots
#     E_i0 = E_ih[K:]
#     E_s0 = E_sh[K:]
#     Channel_g0 = Channel_gh[K:, :, :]
#     #predict the future K data of solar energy of devices,server and chanel gain(prediction phase)
#     future_Es_all = GMM.GMMs(E_sh[0:K],len(E_i0))
#     future_Ei_all = GMM.GMMi(E_ih[0:K],len(E_i0))
#     future_g_all = GMM.GMMg(Channel_gh[0:K],len(E_i0))
#     for j in range(num):
#         [Max_min_Opt0,X0,Y0,Z0,F0] = mec3.MILP(V, M, N, T[0:(len(T) - K)], Dstore_Cap, Estore_Cap,
#                                                                    Dbatt_Cap[K:], Ebatt_Cap[K:], CPU_Cap, E_i0, B_i,
#                                                                    E_s0,
#                                                                    B_s, F_i, Len_slot,
#                                                                    Energy_percpu, Input_size, Workload, Error_coe,
#                                                                    Error_var, Error_thre, Channel_g0, Compu_VMcap,
#                                                                    Channel_band,
#                                                                    Noise_pow, Appro_ratio, VM_consu, Rho)
#         opt = opt + Max_min_Opt0
#
#         #random strategy
#         [X_random, Y_random, Z_random, F_random] = random_decision.randomize_XYZF(X0,Y0,Z0,F0)
#
#         # compute the energy consumption of random strategy
#         energy_device_local_random = 0
#         for i in range(len(X_random)):
#             if i == 0 or i == 1:
#                 energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]*random.choice([0,Appro_ratio])
#             else:
#                 energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]
#
#         energy_upload_random = 0
#         # Tran_pow
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
#         energy_server_random = sum(Z_random[t, i, m] * VM_consu for m in M for i in V for t in list(range(len(T[K:])))) + sum(F_random[t, i, n] * Input_size[i] * Rho for i in V for n in N for t in list(range(len(T[K:]))))
#         energy_upload_device = sum(F_random[t, i, n] * Tran_pow[t, i, n] * Len_slot / Input_size[i] for n in N for t in list(range(len(T[K:])))for i in V)
#         energy_random = energy_server_random + energy_upload_device + energy_device_local_random
#         ran = ran + energy_random
#     sol[0,num_d.index(z)] = opt/num
#     sol[1,num_d.index(z)] = ran/num
#     print(sol)





#threshold
num_time=[10,15,20,25,35]
#number of experiment
num = 5
#temp value for optimal and random solution and matrix for all of them
opt = 0
ran = 0
sol = np.zeros((2,len(num_time)))
for z in num_time:
#Size of the time window
    K = 7
    opt = 0
    ran = 0
    # Device Parameters
    V = list(range(10))
    M = list(range(10))
    N = list(range(10))
    T = list(range(z))
    Dstore_Cap = 1000
    Estore_Cap = 2000
    Ebatt_Cap = np.array([2000] * len(T))
    Dbatt_Cap = np.array([[1000] * len(V)] * len(T))
    #devie cpu capacity
    CPU_Cap = 5e+8#(in cycle)
    B_i = [1e+3] * len(V)
    B_s = 2e+3
    # Computationla capacity of device
    F_i = [2e+9] * len(V)#(in cycle/s)
    Len_slot = 1
    Energy_percpu = 2.5e-12#(in J/cycle)
    Error_coe = [0.005] * len(V)
    Error_var = [2] * len(V)
    Error_thre = z
    Compu_VMcap = [1e+10] * len(M)#（in cycle)
    Channel_band = 1e+7#(in Hz)
    Noise_pow = -87#(dBM)
    Appro_ratio = 0.5
    VM_consu = 1.5#(in J)
    Rho = 1.5e-7#(J/bit)
    # Fixed input data size and workload
    Input_size = [1.5e+5] * len(V)#(in bit)
    Workload = [1e+3] * len(V)#(in cycle/bit)
    # Generate all time slot data for solar energy arrival for nodes and server, channel gain value
    E_ih = Solar.Solar_Value(len(V), T, 900)  # 3000-17000
    E_sh = Solar.Solar_Value(1, T, 900)
    Channel_gh = NetworkBasic.Calculate_Channel_Gain(len(T), len(V), len(N))
    # Compute the optimal solution of all the time slots apart from the history time slots
    E_i0 = E_ih[K:]
    E_s0 = E_sh[K:]
    Channel_g0 = Channel_gh[K:, :, :]
    #predict the future K data of solar energy of devices,server and chanel gain(prediction phase)
    future_Es_all = GMM.GMMs(E_sh[0:K],len(E_i0))
    future_Ei_all = GMM.GMMi(E_ih[0:K],len(E_i0))
    future_g_all = GMM.GMMg(Channel_gh[0:K],len(E_i0))
    for j in range(num):
        [Max_min_Opt0,X0,Y0,Z0,F0] = mec3.MILP(V, M, N, T[0:(len(T) - K)], Dstore_Cap, Estore_Cap,
                                                                   Dbatt_Cap[K:], Ebatt_Cap[K:], CPU_Cap, E_i0, B_i,
                                                                   E_s0,
                                                                   B_s, F_i, Len_slot,
                                                                   Energy_percpu, Input_size, Workload, Error_coe,
                                                                   Error_var, Error_thre, Channel_g0, Compu_VMcap,
                                                                   Channel_band,
                                                                   Noise_pow, Appro_ratio, VM_consu, Rho)

        opt = opt + Max_min_Opt0

        #random strategy
        [X_random, Y_random, Z_random, F_random] = random_decision.randomize_XYZF(X0,Y0,Z0,F0)

        # compute the energy consumption of random strategy
        energy_device_local_random = 0
        #number of approximation mode
        # num_app = sum(Y0)*0.5
        # for i in range(len(X_random)):
        #     if random.choice([0,Appro_ratio]) == Appro_ratio and num_app>0:
        #         num_app = num_app - 1
        #         energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i] * (Appro_ratio)
        #     else:
        #         energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]
        for i in range(len(X_random)):
            if i == 0 :
                energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]*random.choice([0,Appro_ratio+0.42])
            else:
                energy_device_local_random = energy_device_local_random + Input_size[0] * Workload[0] * Energy_percpu * X_random[i]

        energy_upload_random = 0
        # Tran_pow
        Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
        for t in range(len(T[K:])):
            for i in range(len(V)):
                for n in range(len(N)):
                    Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
        energy_server_random = sum(Z_random[t, i, m] * VM_consu for m in M for i in V for t in list(range(len(T[K:])))) + sum(F_random[t, i, n] * Input_size[i] * Rho for i in V for n in N for t in list(range(len(T[K:]))))
        energy_upload_device = sum(F_random[t, i, n] * Tran_pow[t, i, n] * Len_slot / Input_size[i] for n in N for t in list(range(len(T[K:])))for i in V)
        energy_random = energy_server_random + energy_upload_device + energy_device_local_random
        ran = ran + energy_random
    sol[0,num_time.index(z)] = opt/num
    sol[1,num_time.index(z)] = ran/num
    print(sol)