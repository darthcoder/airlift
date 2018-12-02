import numpy as np
import sympy 
import matplotlib.pyplot as plt
from math import pi, sqrt

sympy.init_printing(use_unicode=True)

RHO_AIR = 1.225
RHO_WATER = 1000.0
D = 0.0254
R = D/2
A = pi*(D**2)/4
g = 9.8
MU = 8.9e-4
SIGMA = 7.28e-2
ALPHA = 0.67
Co = 1.2

AIR_EXPT = np.loadtxt("./data/air_standard.txt")
print(AIR_EXPT)
water_arr = np.array([])

Q_air = AIR_EXPT/(RHO_AIR * 3600)
# print(QG)

QF = sympy.symbols("QF")


Bo = ((RHO_WATER)*g*D**2/(SIGMA))
v_ts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))
v_ts = v_ts_dash*sqrt(g*D)

temp = 0
for QG in Q_air:

    left = QF + (1.34*pi*R)*((Co*(QG+QF)/A)+v_ts)*\
           ((MU*QF/(A*SIGMA*(1-(QG/(Co*(QF+QG)+(A*v_ts))))))**(sympy.S("2/3")))

    right = pi*(R**2)*((Co*(QF+QG)/A) + v_ts)

    equation = sympy.Eq(left, right)

    Q_water = sympy.solveset(equation, QF)

    water = list(Q_water)[0]

    temp = water*3600*RHO_WATER
    # print(temp)

    water_arr = np.append(water_arr, temp)    

print(water_arr)    