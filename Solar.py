# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:13:53 2019

@author: Steven
"""
import numpy as np


# Solar Energy harvesting of a PB.  
def Solar_Energy(T, Solar_Panel, Solar_Eff):
    # Initial state 
    State_Set = ['poor', 'good', 'fair', 'excellent']
    E_Mean = {'poor':17.9, 'good':45.6, 'fair':76, 'excellent':94.6}
    E_Sig = {'poor':0.71, 'good':1.48, 'fair':1.55, 'excellent':0.31}
    State = []
    PB_Solar = []
    
    S_Num = np.random.randint(4)
    State.append(State_Set[S_Num])
    PB_Solar.append(np.random.normal(loc=E_Mean[State_Set[S_Num]], scale=E_Sig[State_Set[S_Num]]))
    
    for i in range(len(T)-1):
        # Calculate the harvested energy in slot i
        #PB_Solar[i] = np.random.normal(loc=E_Mean[S_Num], scale=E_Sig[S_Num])
        if State[i] == 'poor':
            State.append(str(np.random.choice(['poor', 'good', 'fair', 'excellent'], size=None, replace=True, p=[0.938,0.057,0.005,0.000])))
        elif State[i] == 'good':
            State.append(str(np.random.choice(['poor', 'good', 'fair', 'excellent'], size=None, replace=True, p=[0.023,0.955,0.022,0.000])))
            
        elif State[i] == 'fair':
            State.append(str(np.random.choice(['poor', 'good', 'fair', 'excellent'], size=None, replace=True, p=[0.000,0.032,0.950,0.018])))
        elif State[i] == 'excellent':
            State.append(str(np.random.choice(['poor', 'good', 'fair', 'excellent'], size=None, replace=True, p=[0.004,0.000,0.023,0.973])))
        else:
            print("State Wrong")
        PB_Solar.append(np.random.normal(loc=E_Mean[State[i+1]], scale=E_Sig[State[i+1]]))
        
    # Consider pannel size and conversion efficiency.  
    for i in range(len(PB_Solar)):
        PB_Solar[i] =  PB_Solar[i]*Solar_Panel*Solar_Eff

    return PB_Solar

# Calculate multiple PBs' solar energy.  
def Solar_Value(Num_Node, T, Solar_Panel):
    Solar_Eff = 0.2 #Solar panel conversion efficiency 20%
    Node_Solar = np.zeros([len(T), Num_Node])
    for i in range(Num_Node):
        Node_Solar[:,i] = Solar_Energy(T, Solar_Panel, Solar_Eff)
    
    return Node_Solar




