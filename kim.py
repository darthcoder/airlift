# Kim, Sohn and Hwang's paper from 2014 is simulated here:
# The main formula is:
#
#   ,   ,            ,      ,                              ,2
# Q  = V   - (C    V   +  V   )(1 -  \alpha / (1 + 0.5 f V   ) ) .... (1)
#  L    M      0    M      TS                             M
#
#          ,     ,      ,
# Where, V   =  Q   + Q
#         M      G     L
#
# where,
#     ,                   __
#   Q    =  Q     /  (A |/gD   )
#    L/G     L/g
#
#  and
#      ,                    -1          -2
#    V   = 0.352(1 - 3.18 Bo   -14.77 Bo   )
#     TS
#                      2
#  and        \rho g D
#       Bo = -----------
#              \sigma
#
# Q   is the unknown and it is a factor in V  which makes this a problem
#  L                                        M
# for iterative solution.

#--------------------------------------------------------------------
#                       ,        ,
#   Note the ranges of Q   and  Q   need to be identified correctly
#                       g        L
#   from Fig. 9, pg 202 of the paper by Kim et al
#
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt
from functions import vm, right_hs#, key

# L = 0.5
L = 3.75
g = 9.81
#D = np.array([0.008, 0.011, 0.018, 0.024]
# D = 0.008
D = 0.0254
A = pi*(D**2)/4
# alpha = 0.9
alpha = 0.67
#co = 1.2

sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4 #viscosity of water at 25 C in Pa.s

Bo = ((rho_water)*g*D**2/(sigma))
v_ts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))

# ndiv = 200
# Q_g_dash = np.linspace(0.1, 10, ndiv)
# Q_l_dash_try = np.linspace(0.01, 100, 10000)
# Q_l_dash = np.zeros(ndiv)
#Qldash = np.empty(len(D))

# temp = 0
# for qgdash in Q_g_dash:
#     for qldash in Q_l_dash_try:
#         vm_dash = vm(qgdash,qldash)

#         ql = qldash*A*sqrt(g*D)
#         vl = ql/A

#         Re = rho_water*vl*D/mu

#         if (Re < 2300):
#             co = 2
#             f = 64/Re
            
#         else:
#             co = 1.2
#             f = 0.316/(pow(Re, 0.25))
        
#         #k = key(f, vm_dash)
#         #lhs = qldash * k
#         lhs = qldash
#         #rhs = k*vm_dash - (co*vm_dash + v_ts_dash)*(k-alpha)

#         rhs = right_hs(vm_dash, co, v_ts_dash, alpha, f)

#         diff = abs(lhs - rhs)

#         if (diff < 0.001):
#             temp = qldash
#             break
        
#     Q_l_dash = np.append(Q_l_dash, temp)


# Q_l_dash = np.trim_zeros(Q_l_dash)
#print(Q_l_dash)    

# plt.yscale('log')
# plt.xscale('log')
# plt.plot(Q_g_dash,Q_l_dash,'ro')
# plt.show()

# np.savetxt('./data/kim_g.txt',Q_g_dash)
# np.savetxt("./data/kim_l_8mm_sub0_9.txt",Q_l_dash)

air_kassab = np.loadtxt("./data/air_standard.txt")
Qg = np.zeros(len(air_kassab))
Qg = air_kassab / ( 3600 * rho_air )
Qg_dsh = Qg / (A*sqrt(g*D))

# print(Qg_dsh)
ndivi = 100000
# Ql_dsh = np.array([])
Ql = np.array([])
Ql_dsh = np.array([])
Ql_try = np.linspace(0.01, 200, ndivi)

tempy = 0
for qg in Qg_dsh:
    for ql_dash in Ql_try:
        vm_dash = vm(ql_dash, qg)
        ql = ql_dash*A*sqrt(g*D)
        vl = ql/A
        qg_air = qg*A*sqrt(g*D)
        vg = qg_air / A
        vm1 = vl+vg
        Re = rho_air*vg*D/mu

        if (Re < 2300):
            co = 2
            f = 64/Re
            
        else:
            co = 1.2
            f = 0.316/(pow(Re, 0.25))

        lhs = ql_dash
        #rhs = k*vm_dash - (co*vm_dash + v_ts_dash)*(k-alpha)

        rhs = right_hs(vm_dash, co, v_ts_dash, alpha, f)

        diff = abs(lhs - rhs)

        if (diff < 0.001):
            tempy = ql_dash
            # tempy = ql
            break
        
    Ql_dsh = np.append(Ql_dsh, tempy)
    # Ql = np.append(Ql, tempy)

factor = A * sqrt(g*D)

# print(Ql_dsh)
Ql = Ql_dsh * factor
print(Ql)
W = Ql * rho_water * 3600 
# W = Ql * rho_water 
# W[0] = 4000
print(W)


# plt.yscale('log')
# plt.xscale('log')

# z = np.polyfit(air_kassab, W, 4)
# print(len(z))
# print(z)
# print(len(air_kassab))
# fit = z[0] + z[1] * air_kassab + z[2] * (air_kassab**2) \
#    + z[3] * (air_kassab**3) + z[4] * (air_kassab**4)
# plt.plot()
# plt.plot(Qg_dsh, Ql_dsh)
# plt.plot(air_kassab, fit)
# plt.show()
# print(fit)
# plt.plot(air_kassab, W)
# plt.show()

# np.savetxt("./data/kim_water_standard.txt", W)
