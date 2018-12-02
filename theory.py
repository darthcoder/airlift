"""
This program models the theory that I developed during
the Puja vacation so that I can plot it against other
theories and see how (in)accurate my theory is. I still
have to think about how to get a log relation.
"""

from math import pi, sqrt
import numpy as np
# import matplotlib.pyplot as plt


RHO_AIR = 1.225
RHO_WATER = 1000.0
D = 0.0254
R = D/2
A = pi*(D**2)/4
g = 9.8
MU = 8.9e-4
SIGMA = 7.28e-2
ALPHA = 0.67


AIR_EXPT = np.loadtxt("./data/air_standard.txt")

# SLICE = AIR_EXPT[3:]

# QG = SLICE/(RHO_AIR * 3600)
QG = AIR_EXPT/(RHO_AIR * 3600)
QF_try = np.linspace(0.0000001,0.01,1000000)
QF = np.array([])
# QF = 0.345*pi*(R**2)*sqrt(g*D*(RHO_WATER - RHO_AIR)/RHO_WATER) -(0.690*0.67)* \
    # sqrt(g*D*(RHO_WATER - RHO_AIR)/RHO_WATER)* ((MU*QG/(A*SIGMA)*(1-ALPHA))**(2/3))

# this is the formula i was using earlier
# QF = QG - (1.34*QG*((MU*QG/(A*SIGMA*(1-ALPHA)))**(2/3))/R)

# print(QG)
# print(QF)

# here the mass flow rate was being computed
# W = QF*RHO_WATER*3600
# print(len(W))
# np.savetxt("./data/theory_water.txt", W)

temp = 0
for qg in QG:
    for qf in QF_try:
        lhs = qf

        rhs = qg - (1.34*qg*((MU*qg/(A*SIGMA*(1-ALPHA)))**(2/3))/R)

        diff = abs(lhs - rhs)

        if (diff < 0.0001):
            temp = qf
            break

    QF = np.append(QF, temp)


W = QF*RHO_WATER*3600
print(W)







