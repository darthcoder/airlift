import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt
from functions import righthandside, sfactor, lefths

# length of the pipe is 168 in = 4.27m
# dia of the pipe is 25.4 mm (1 in)
# Submergence ratio, ar has four values = 0.707, 0.629, 0.532 and 0.442



L = 14.01
D = 0.082
A = pi * (D**2) / 4
rho_air = 0.07
rho_water = 62.2
mu = 6e-4
# submergence ratio: 0.707
ar = 0.707

# Pa = 2116.22
# P1 = 2.7e5
g = 32.174

#v1 = sqrt((2/rho_water)*(Pa - P1 + (rho_water * g * L * ar)))

ndiv = 100
step = 0.01
stride = 0.001
ndivision = 10000 # this is for Ql_try only

# in cubic meter (converted from cubic feet)
Qg = np.linspace(0.01, 20, ndiv)
Ql_try = np.linspace(0.001, 20, ndivision)

# Qg and Ql_try will be in cubic feet per second
# Qg = np.linspace(0.01,10,ndiv)
# Qg = range(0.01, 0.2, step)
# Ql_try = range(0.001,0.02,ndivision)
# Ql = []

Ql = np.array([])

temp = 0

for qg in Qg:
    for ql in Ql_try:
        v1 = ql/(A)
        # s = 1.2 + 0.2 * (qg/ql) + 0.35 * (sqrt(g*D))/(v1)
        s = sfactor(qg, ql, g, D, v1)
        Re = rho_water*v1*D/mu 
        f = 0.316/(pow(Re, 0.25))
        k = 4*f*L/D

        # lhs = ar - (1/(1+(qg/(s*ql))))
        lhs = lefths(ar, s, qg, ql) 
        # rhs = ((v1**2)/(2*g*L))*[(k + 1) + (k + 2)*(qg/ql)]
        rhs = righthandside(v1, g, L, f, qg, ql)

        diff = abs(lhs - rhs)

        if (diff < 0.0005):
            temp = ql
            break
    
    # Ql = np.append(Ql, temp)
    Ql = Ql.append(temp)

    
Ql1 = np.array(Ql)


print(Ql)
print(len(Qg))
print(len(Ql))


plt.plot(Qg,Ql,'ro')
plt.show()