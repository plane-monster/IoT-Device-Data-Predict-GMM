import random
from pyomo.environ import *
import numpy as np

def randomize_XYZF(X,Y,Z,F):
    #randomize X on the local excuting task
    newX = [0]*len(X)
    for i in range(len(X)):
        if X[i] == 1:
            newX[i]=random.choice([0,1])

    #randomize Z
    # Get the sizes of the dimensions
    num_slots, num_devices, num_VMs = Z.shape
    T = list(range(num_slots))
    VM_allocate = []
    device_upload = []
    for t in range(num_slots):
        for i in range(num_devices):
            for m in range(num_VMs):
                if Z[t, i, m] == 1:
                    VM_allocate.append(m)
                    device_upload.append(i)
    VM_allocate = np.unique(VM_allocate)
    device_upload = np.unique(device_upload)
    VM_all = list(range(num_VMs))
    device_all = list(range(num_devices))
    VM_non_allocate = VM_all.copy()
    device_non_upload = device_all.copy()
    newZ = np.zeros_like(Z)
    for m in VM_allocate:
        VM_non_allocate.remove(m)
    for i in device_upload:
        device_non_upload.remove(i)
    #randomize the VM for upload the task alredy
    for t in range(num_slots):
        for i in range(num_devices):
            for m in range(num_VMs):
                if Z[t, i, m] == 1:
                    VM_index1 = random.choice(VM_non_allocate)
                    newZ[t,i,VM_index1] = 1
    #additional 1 for the X unused
    for i in range(num_devices):
        if X[i]==0 and i in device_upload:
            VM_index2 = random.choice(VM_allocate)
            t_index1 = random.choice(T)
            newZ[t_index1,i,VM_index2] = 1

    #randomize F
    newF = np.zeros_like(F)
    # Get the sizes of the dimensions
    num_slots, num_devices, num_channels = F.shape
    channels = list(range(num_channels))
    for t in range(num_slots):
        for i in range(num_devices):
            for n in range(num_channels):
                if F[t,i,n] == 1:
                    if t>0:
                        t_index = random.choice(T[0:t])
                        newF[t_index,i,n]=1
    #additional 1 for the X unused
    for i in range(num_devices):
        if X[i]==0 and i in device_upload:
            channel_index = random.choice(channels)
            newF[0,i,channel_index] = 1


    #randomize Y
    newY = np.zeros_like(Y)
    for i in range(len(X)):
        if newX[i] == 1:
            newY[i] = np.random.choice([0, 1])
        else:
            newY[i] = 0

    return[X,Y,Z,F]






