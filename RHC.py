import Solar
import NetworkBasic
import numpy as np
import random
import GMM


# #number of devices
# num_v=[8,12,16,18,20,24]
# #number of experiment
# num = 5
# #temp value for optimal, heuristic and random solution and matrix for all of them
# heu = 0
# sol = np.zeros(len(num_v))
# for z in num_v:
# #Size of the time window
#     K = 7
#     heu = 0
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
#         # heuristic solution
#         # X decision
#         X = [0] * len(V)
#         energy_vfuture = [0] * len(V)
#         for i in range(len(V)):
#             energy_vfuture[i] = min(future_Ei_all[:, i])
#             if energy_vfuture[i] >= Input_size[i] * Workload[i] * Energy_percpu and Input_size[0] * Workload[0] <= F_i[i] * len(future_Ei_all):
#                 X[i] = 1
#                 # compute the energy of excuting locally and assume that each have approcimation mode
#             energy_device_local_heu = 0
#             for i in range(len(X)):
#                 energy_device_local_heu = energy_device_local_heu + Input_size[0] * Workload[0] * Energy_percpu * X[i] * random.choice([1,Appro_ratio])
#         # Z and F decision
#         # Actually, for the given data , and require each iteration have excute the task uploadly
#         energy_upload_all = 0
#         I_upload = []
#         for x in range(len(X)):
#             if X[x] == 0:
#                 I_upload.append(x)
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
#         for i in I_upload:
#             energy_upload_all = VM_consu + Input_size[i] * Rho + Tran_pow[0, i, 0] / Input_size[i] + energy_upload_all
#         heu = heu + energy_upload_all + energy_device_local_heu
#     sol[num_v.index(z)] = heu/num
#     print(sol)

# #number of CHANNELS
# num_n=[8,12,16,18,20,24]
# #number of experiment
# num = 5
# #temp value for optimal, heuristic and random solution and matrix for all of them
# heu = 0
# sol = np.zeros(len(num_n))
# for z in num_n:
# #Size of the time window
#     heu = 0
#     K = 7
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
#         # heuristic solution
#         # X decision
#         X = [0] * len(V)
#         energy_vfuture = [0] * len(V)
#         for i in range(len(V)):
#             energy_vfuture[i] = min(future_Ei_all[:, i])
#             if energy_vfuture[i] >= Input_size[i] * Workload[i] * Energy_percpu and Input_size[0] * Workload[0] <= F_i[i] * len(future_Ei_all):
#                 X[i] = 1
#                 # compute the energy of excuting locally and assume that each have approcimation mode
#             energy_device_local_heu = 0
#             for i in range(len(X)):
#                 energy_device_local_heu = energy_device_local_heu + Input_size[0] * Workload[0] * Energy_percpu * X[i] * random.choice([1,Appro_ratio])
#         # Z and F decision
#         # Actually, for the given data , and require each iteration have excute the task uploadly
#         energy_upload_all = 0
#         I_upload = []
#         for x in range(len(X)):
#             if X[x] == 0:
#                 I_upload.append(x)
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
#         for i in I_upload:
#             energy_upload_all = VM_consu + Input_size[i] * Rho + Tran_pow[0, i, 0] / Input_size[i] + energy_upload_all
#         print(energy_upload_all)
#         print(energy_device_local_heu)
#         heu = heu + energy_upload_all + energy_device_local_heu
#     sol[num_n.index(z)] = heu/num
#     print(sol)

#
# #eta approximation ratio
# eta=[0.1,0.3,0.5,0.7,0.9]
# #number of experiment
# num = 5
# #temp value for optimal, heuristic and random solution and matrix for all of them
# heu = 0
# sol = np.zeros(len(eta))
# for z in eta:
# #Size of the time window
#     heu = 0
#     K = 7
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
#     Appro_ratio = z
#     VM_consu = 1.5#(in J)
#     Rho = 1.5e-7#(J/bit)
#     # Fixed input data size and workload
#     Input_size = [1.5e+5] * len(V)#(in bit)
#     Workload = [1e+3] * len(V)#(in cycle/bit)
#
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
#         # heuristic solution
#         # X decision
#         X = [0] * len(V)
#         energy_vfuture = [0] * len(V)
#         for i in range(len(V)):
#             energy_vfuture[i] = min(future_Ei_all[:, i])
#             if energy_vfuture[i] >= Input_size[i] * Workload[i] * Energy_percpu and Input_size[0] * Workload[0] <= F_i[i] * len(future_Ei_all):
#                 X[i] = 1
#                 # compute the energy of excuting locally and assume that each have approcimation mode
#             energy_device_local_heu = 0
#             for i in range(len(X)):
#                 energy_device_local_heu = energy_device_local_heu + Input_size[0] * Workload[0] * Energy_percpu * X[i] * random.choice([1,Appro_ratio])
#         # Z and F decision
#         # Actually, for the given data , and require each iteration have excute the task uploadly
#         energy_upload_all = 0
#         I_upload = []
#         for x in range(len(X)):
#             if X[x] == 0:
#                 I_upload.append(x)
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     #in watts
#                     Tran_pow[t, i, n] = 1e-3*pow(10,((pow(2, Input_size[i] / Channel_band) - 1)* Noise_pow-30)/10)  / Channel_g0[t, i, n]
#         for i in I_upload:
#             energy_upload_all = VM_consu + Input_size[i] * Rho + Tran_pow[0, i, 0] / Input_size[i] + energy_upload_all
#         heu = heu + energy_upload_all + energy_device_local_heu
#     sol[eta.index(z)] = heu/num
#     print(sol)

# #Data size
# num_d=[2e+5,6e+5,10e+5,12e+5]
# #number of experiment
# num = 5
# #temp value for optimal, heuristic and random solution and matrix for all of them
# heu = 0
# sol = np.zeros(len(num_d))
# for z in num_d:
# #Size of the time window
#     heu = 0
#     K = 7
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
#         # heuristic solution
#         # X decision
#         X = [0] * len(V)
#         energy_vfuture = [0] * len(V)
#         for i in range(len(V)):
#             energy_vfuture[i] = min(future_Ei_all[:, i])
#             if energy_vfuture[i] >= Input_size[i] * Workload[i] * Energy_percpu and Input_size[0] * Workload[0] <= F_i[i] * len(future_Ei_all):
#                 X[i] = 1
#                 # compute the energy of excuting locally and assume that each have approcimation mode
#             energy_device_local_heu = 0
#             for i in range(len(X)):
#                 energy_device_local_heu = energy_device_local_heu + Input_size[0] * Workload[0] * Energy_percpu * X[i] * random.choice([1,Appro_ratio])
#         # Z and F decision
#         # Actually, for the given data , and require each iteration have excute the task uploadly
#         energy_upload_all = 0
#         I_upload = []
#         for x in range(len(X)):
#             if X[x] == 0:
#                 I_upload.append(x)
#         Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
#         for t in range(len(T[K:])):
#             for i in range(len(V)):
#                 for n in range(len(N)):
#                     Tran_pow[t, i, n] = (pow(2, Input_size[i] / Channel_band) - 1) * Noise_pow / Channel_g0[t, i, n]
#         for i in I_upload:
#             energy_upload_all = VM_consu + Input_size[i] * Rho + Tran_pow[0, i, 0] / Input_size[i] + energy_upload_all
#         print(energy_upload_all)
#         print(energy_device_local_heu)
#         heu = heu + energy_upload_all + energy_device_local_heu
#     sol[num_d.index(z)] = heu/num
#     print(sol)


#time slot
num_time=[10,15,20,25,35]
#number of experiment
num = 5
#temp value for optimal, heuristic and random solution and matrix for all of them
heu = 0
sol = np.zeros(len(num_time))
for z in num_time:
#Size of the time window
    heu = 0
    K = 7
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
    Error_var = [1.2] * len(V)
    Error_thre = 0.02
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
        # heuristic solution
        # X decision
        X = [0] * len(V)
        energy_vfuture = [0] * len(V)
        for i in range(len(V)):
            energy_vfuture[i] = min(future_Ei_all[:, i])
            if energy_vfuture[i] >= Input_size[i] * Workload[i] * Energy_percpu and Input_size[0] * Workload[0] <= F_i[i] * len(future_Ei_all):
                X[i] = 1
                # compute the energy of excuting locally and assume that each have approcimation mode
            energy_device_local_heu = 0
            for i in range(len(X)):
                energy_device_local_heu = energy_device_local_heu + Input_size[0] * Workload[0] * Energy_percpu * X[i] * random.choice([1,Appro_ratio])
        # Z and F decision
        # Actually, for the given data , and require each iteration have excute the task uploadly
        energy_upload_all = 0
        I_upload = []
        for x in range(len(X)):
            if X[x] == 0:
                I_upload.append(x)
        Tran_pow = np.zeros((len(T[K:]), len(V), len(N)))  # $P_{i}^{t}$
        for t in range(len(T[K:])):
            for i in range(len(V)):
                for n in range(len(N)):
                    Tran_pow[t, i, n] = 1e-3*pow(10,((pow(2, Input_size[i] / Channel_band) - 1)* Noise_pow-30)/10)/ Channel_g0[t, i, n]
        #search for the least Tranpow of the given device
        Tran_pow_least = [100]*len(V)
        for i in I_upload:
            for t in range(len(T[K:])):
                for n in range(len(N)):
                    if Tran_pow[t,i,n] < Tran_pow_least[i]:
                        Tran_pow_least[i] = Tran_pow[t,i,n]
        for i in I_upload:
            energy_upload_all = VM_consu + Input_size[i] * Rho + Tran_pow_least[i] / Input_size[i] + energy_upload_all
        heu = heu + energy_upload_all + energy_device_local_heu

    sol[num_time.index(z)] = heu/num
    print(sol)





