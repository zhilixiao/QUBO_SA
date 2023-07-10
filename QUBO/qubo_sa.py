import numpy as np
import random as rand
import math


# functions for transforming the adjacency matrix A to Qubo matrix Q
def AtoQ(A):
    Q = 2 * np.triu(A)
    #Q = np.triu(A)
    np.fill_diagonal(Q, -sum(A))
    return Q

def modQ(Q):
    newQ = np.triu(Q) + np.triu(Q).T
    np.fill_diagonal(newQ, np.diag(Q))
    return newQ


def qubo_SA(Q, init_heat, heat_max, delta_heat):
    Q = modQ(Q)
    N = int(np.shape(Q)[0])
    heat = init_heat
    x = np.ones((1,N), dtype = bool)
    x_best = np.ones((1,N), dtype = bool)
    best_E = 0
    #best_cut_trace = np.zeros((math.ceil(heat_max/100/2e-3)+1))
    cur_E = 0

    iter = 0
    while heat < heat_max:
        n = rand.randint(0,N-1)
        Qij = Q[n,:]

        
        x_new = x.copy()
        x_new[0,n] = ~x[0,n]
        
        x_old = int(x[0,n] * 1)
        x_tmp = int(~x[0,n] * 1)
        
        # old = np.sum(np.multiply((x_old * x), Qij))
        # new = np.sum(np.multiply((x_tmp * x_new), Qij))
        # chg = float(new - old)

        chg = float(np.inner((x_tmp * x_new - x_old * x), Qij))

        r = rand.random()

        if r <= np.exp(heat*chg/(best_E + 1)):

            x = x_new.copy()
            cur_E += chg

            if cur_E < best_E:
                x_best = x.copy()
                best_E = cur_E
            
        heat += delta_heat

    return best_E, x_best

