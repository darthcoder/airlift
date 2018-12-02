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

import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt
from functions import vm, right_hs

L = 0.5
g = 9.81
D = 0.008 # 8 mm
A = pi*D**2/4
alpha = 0.8
co = 1.2

sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4 #viscosity of water at 25 C in Pa.s

Bo = ((rho_water)*g*D**2/(sigma))
v_ts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))


ndiv = 200

# Flow rate of gas
Q_g_dash = np.linspace(0.02, 100, ndiv)

# A long array for trial and error
Q_l_dash_try = np.linspace(0.01, 100, 1000)

# the array where flow rate of liquid will be stored
Q_l_dash = np.zeros(ndiv)
# if (len(Q_g_dash) == len(Q_l_dash)):
#     print("Were in business")

for i in np.arange(ndiv):
    temp = 0
    for j in np.arange(1000):
        #    ,        ,        ,
        #  v     =  Q     +  Q
        #   m        g        L

        v_m_dash = vm()
        #v_m_dash = Q_g_dash[i] + Q_l_dash_try[j]
        #print(v_m_dash)

        # for calculating the Reynolds number we need the velocity, so
        #                        ,
        # we first convert the Q    to water flow rate.
        #                       L


        ql = Q_l_dash_try[j]*A*sqrt(g*D)

        # since velocity*area of flow = volumetric flow rate

        vl = ql/(A)

        # from the definition of Reynolds number, Re
        Re = rho_water*vl*D/mu

        # defining the friction factor, f depending on Re
        if (Re < 2300):
            f = 64/Re
            #print(f)

        else:
            f = 0.316/(pow(Re, 0.25))


        # we try to solve eq (1) iteratively
        lhs = Q_l_dash_try[j]
        #rhs = v_m_dash - (co*v_m_dash + v_ts_dash) * (1 -(alpha/(1 + 0.5*f*(v_m_dash**2))))
        rhs = (Q_g_dash[i] + Q_l_dash_try[j]) - (co*(Q_g_dash[i] + Q_l_dash_try[j]) \
        * v_ts_dash)*(1 - (alpha/(1 + 0.5*f*((Q_g_dash[i] + Q_l_dash_try[j])**2))))
        #print(lhs-rhs)
        #print(Q_g_dash[i])
        diff = abs(lhs - rhs)
        if (diff < 1):
            qgdash = Q_g_dash[i]
            print(qgdash)
            temp = j
            break

    #print(lhs)
    #print(temp)

    Q_l_dash = np.append(Q_l_dash, Q_l_dash_try[temp])


Q_l_dash = np.trim_zeros(Q_l_dash)
for i in np.arange(len(Q_l_dash)):
    if Q_l_dash[i] == 0.01:
        print(i)

# plt.plot(Q_g_dash, Q_l_dash, 'r--')
# plt.show()
