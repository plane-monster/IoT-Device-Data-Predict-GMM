# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:50:15 2019

@author: Steven
"""

import numpy as np
import math
import random



def Calculate_Channel_Gain(Num_T, Num_VG, Num_VD):
    
    Distance_Matrix = np.zeros([Num_VG, Num_VD])
    for i in range(Num_VG):
        for j in range(Num_VD):
            Distance_Matrix[i][j] = 10 # Distance between sensor and gateway is 10 m.
    
    Link_Channel_mW = np.zeros([Num_T, Num_VG, Num_VD, ]) 
    
    Alpha = 2.5 # Path Loss Exponent
    d_0 = 1 #d_0 is one meter
    c_0 = -20 #path loss at one meter.
    c_0_mW = np.power(10,(c_0/10))
    
    for t in range(Num_T):
        for i in range(Num_VG):
            for j in range(Num_VD):
                h = np.random.exponential(1)
                # Unit: mW
                Link_Channel_mW[t,i,j] = h*c_0_mW*np.power(Distance_Matrix[i][j],-Alpha)
    
    '''
    # We don't need.  See (11)'
    W = 200000#1000000 # Bandwidth is 1 MHz.  
    N_0 = np.power(10,-95/10) # Noise is -95 dBm.  Tranfers dBm to mW
    
    for t in range(Num_T):
        for i in range(Num_VG):
            for j in range(Num_VD):
                if Wireless_Link_Matrix[i][j] == 1:
                    VD_P[t][i][j] = (math.pow( 2, VD_RateCap/W )-1)*N_0/Link_Channel_mW[t,i,j]
    
    '''
    #Link_Cap_Matrix = Shannon_Cap(Num_T, Num_VD, Num_VG, Wireless_Link_Matrix, Link_Channel_mW, VD_P)
    
    return Link_Channel_mW



'''
def Topology_Matrix(Num_N, Link_Matrix, Num_V_Max, Num_R, R_LinkConnect_Set, R_V_CPU):
    Link_Para = np.zeros([Num_N, Num_N])
    for i in range(Num_N):
        for j in range(Num_N): 
            if Link_Matrix[i][j] == 1:
                Link_Para[i][j] = 1
    
    Virtual_Link_Para = np.zeros([Num_R, Num_V_Max, Num_V_Max])
    for r in range(Num_R):
        for u in range(Num_V_Max):
            for v in range(Num_V_Max):
                if R_LinkConnect_Set[r][u][v] == 1:
                    Virtual_Link_Para[r][u][v] = 1
    
    
    # Virtual node label.
    Virtual_Node_Para = np.zeros([Num_R, Num_V_Max])
    for r in range(Num_R):
        for u in range(Num_V_Max):
            if R_V_CPU[r][u] == 0:
                Virtual_Node_Para[r][u] = 0
            else:
                Virtual_Node_Para[r][u] = 1
    
    return Link_Para, Virtual_Link_Para, Virtual_Node_Para
'''
