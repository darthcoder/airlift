# The formulae of Reinemann are rather similar to Kim et al. 
# the major exception is that there is also a term for void 
# fraction in Reinemann's formulation. 
#
#                                   f     ,    , 2
#   \alpha = (1 - \epsilon)[ 1 +  ----- (Q  + Q ) ] 
#                                   2     L    G
#   
#                        Z
#                         S
#    \alpha     =    -----------
#             
#                     Z    +  Z
#                      S       L
#
#                                        ,
#                                       Q 
#                                        G
#       \epsilon   =     -------------------------
#                                  ,    ,     ,
#                            1.2 (Q  + Q ) + V 
#                                  L    G     TS
#   where,    
#             , 
#            V     has the same expression as kim.py
#             TS 
#  
# Reinemann hasn't produced plots of Q_l vs Q_g so that will have to be 
# made. 

import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt
from functions import epsilon, righths

L = 1.8
g = 9.81
#D = varies from 3.18 to 19.1 mm incl. 6.35 and 9.53
D = 0.006
A = pi*D**2/4
alpha = 0.6

co = 1.2 # only one formula is used in this paper
sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4 #viscosity of water at 25 C in Pa.s

Bo = ((rho_water)*g*D**2/(sigma))
vts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))

ndiv = 100
Qg_dsh = np.linspace(0.5, 7, ndiv)
Ql_dash_try = np.linspace(0.1, 100, 700000)
#Ql_dash = np.zeros(ndiv)
Ql_dash = np.array([])
# cant use np.zeros as its giving error - when using np.trim_zeros, 
# some of the elements also get trimmed. 

temp = 0

for qgdash in Qg_dsh:
    for qldash in Ql_dash_try:
        ql = qldash*A*sqrt(g*D)
        vl = ql/A

        Re = rho_water*vl*D/mu

        f = 0.316/(pow(Re, 0.25))

        lhs = alpha
        eps = epsilon(qldash,qgdash,vts_dash)
        rhs = righths(qldash, qgdash, eps, f)
        
        diff = abs(lhs - rhs)

        if (diff < 0.001):
            temp = qldash
            break
        
    Ql_dash = np.append(Ql_dash, temp)

# print(len(Ql_dash))
# Ql_dash = np.trim_zeros(Ql_dash,'f')
# print(Ql_dash)
# print(len(Qg_dsh))
# print(len(Ql_dash))

plt.plot(Qg_dsh,Ql_dash,'ro', label = '$Q_l\'$ vs $Q_g\'$')
plt.legend()
plt.show()

np.savetxt('./data/rei_g.txt', Qg_dsh)
np.savetxt('./data/rei_l_6mm_sub0_6.txt', Ql_dash)



#--------------------------------------------------------------------------
# L = 3.75
# g = 9.81
# #D = varies from 3.18 to 19.1 mm incl. 6.35 and 9.53
# D = 0.0254
# A = pi*D**2/4
# alpha = 0.67

# co = 1.2 # only one formula is used in this paper
# sigma = 7.28e-2
# rho_water = 1000
# rho_air = 1.225
# mu = 8.9e-4 #viscosity of water at 25 C in Pa.s

# Bo = ((rho_water)*g*D**2/(sigma))
# vts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))

# air_kassab = np.loadtxt("./data/air_standard.txt")
# Qg = np.zeros(len(air_kassab))
# Qg = air_kassab / ( 3600 * rho_air )
# Qg_dash = Qg / (A*sqrt(g*D))
# # print(Qg_dash)

# # print(Qg_dsh)
# ndivi = 700000
# # Ql_dsh = np.array([])
# Ql = np.array([])
# Ql_try = np.linspace(0.1, 100, ndivi)

# tempy = 0

# for qgdash in Qg_dash:
#     for qldash in Ql_try:
#         ql = qldash*A*sqrt(g*D)
#         vl = ql/A
#         qg_air = qgdash*A*sqrt(g*D)
#         vg = qg_air / A
#         # Re = rho_air*vg*D/mu
#         Re = rho_water*vl*D/mu

#         if (Re < 2300):
#             # co = 2
#             f = 64/Re
            
#         else:
#             # co = 1.2
#             f = 0.316/(pow(Re, 0.25))
#         # f = 0.316/(pow(Re, 0.25))

#         lhs = alpha
#         eps = epsilon(qldash,qgdash,vts_dash)
#         rhs = righths(qldash, qgdash, eps, f)
        
#         diff = abs(lhs - rhs)

#         if (diff < 0.001):
#             tempy = ql
#             break
        
#     Ql = np.append(Ql, tempy)

# W = Ql * rho_water * 3600
# # print(W)
# np.savetxt("./data/reinemann_water_standard.txt",W)
# # water_kassab = np.loadtxt("./data/kassab_water_kph.txt")
# # water_kassab1 = water_kassab[3:]

# # plt.plot(air_kassab,W)
# # plt.plot(air_kassab, water_kassab1, 'ro')
# # plt.show()



