# This attempt uses implicit formulation (Q_f on both sides of the equation)
# It is a bit more complex than the previous theory

import numpy as np
from math import pi, pow
# from functions import vm #self-made module

L = 3.75
g = 9.81
D = 0.0254
A = pi*(D**2)/4
alpha = 0.67

sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4
co = 1.2

Bo = ((rho_water)*g*D**2/(sigma))
v_ts = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))


air_kassab = np.loadtxt("./data/air_standard.txt")
Qg = np.zeros(len(air_kassab))
Qg = air_kassab / ( 3600 * rho_air )

ndivi = 100000
Ql = np.array([])
Ql_try = np.linspace(0.0001, 10, ndivi)


tempy = 0

for qg in Qg:
    for qltry in Ql_try:
        vm = (qg + qltry)/A

        lhs = qltry

        u = co*vm + v_ts

        ca = mu*u/sigma   # capillary number
        delta = 0.67 * pow(ca,(2/3))

        rhs = A*u - 2*pi*(D/2)*delta*u

        diff = abs(rhs - lhs)

        if (diff < 0.01):
            tempy = qltry
            break

    Ql = np.append(Ql, tempy)


W = Ql * rho_water * 3600 
print(W)



