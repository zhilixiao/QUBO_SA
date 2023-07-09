import numpy as np
import random as rand
import math

def maxcut_SA(A, init_heat, heat_max, delta_heat):
    N = int(np.shape(A)[0])
    heat = init_heat
    v = np.ones((1,N))
    v_best = np.ones((1,N))
    best = 0
    #best_cut_trace = np.zeros((math.ceil(heat_max/100/2e-3)+1))
    cur_cut = 0

    iter = 0
    while heat < heat_max:
        n = rand.randint(0,N-1)
    
        v_tmp = -v[0,n] 
        e_tmp = A[n,:]
        chg = int(-v_tmp * np.inner(e_tmp,v))
    
        r = rand.random()

        if r <= np.exp(heat*chg/(best + 1)):
            v[0,n] = v_tmp
            cur_cut += chg
        
            if cur_cut > best:
                v_best = v.copy()
                best = cur_cut
            
        heat += delta_heat


    max_cut = np.sum(np.sum(np.multiply(A, 1 - v_best.T@v_best)))/4


    return max_cut, v_best