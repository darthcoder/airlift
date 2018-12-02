import numpy as np
import sympy 
import matplotlib.pyplot as plt
# from math import sqrt
sympy.init_printing(use_unicode=True)

rho_air = 1.225
rho_water = 1000
D = 0.0254
R = D/2
A = np.pi*D**2/4
g = 9.8
mu = 8.9e-4
sigma = 7.28e-2
alpha = 0.67
Co = 1.2
L = 3.75


# air_expt = np.loadtxt("./data/air_standard.txt")
air_expt = np.loadtxt("./data/air_standard.txt")[3]
water_arr = np.array([])

Q_air = air_expt/(rho_air*3600)

Qf = sympy.symbols("Qf")

Bo = rho_water*g*(D**2)/sigma

v_ts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))
v_ts = v_ts_dash*np.sqrt(g*D)


temp = 0 
# for Qg in Q_air:
#     left = alpha
#     Vm = (Qg + Qf)/A
#     epsilon = Qg/((Co*Vm + v_ts)*A)
#     sqep = epsilon**(0.5)
#     beta = 1 - (2/3)*(R/L)*sqep 

#     vf = Qf/A 
#     Re = rho_water*vf*D/mu

#     f = 0.316/(Re**(1/4))

#     expr = f*(Vm**2)/(2*g*D)

#     right = (1-epsilon)*(1+((1-beta)*expr+beta*(1-epsilon)))

#     equation = sympy.Eq(left, right)

#     Q_water = sympy.solveset(equation, Qf)
#     print(Q_water)
#     water = list(Q_water)[0]

#     temp = water*3600*RHO_WATER

#     water_arr = np.append(water_arr, temp)  

# print(water_arr)

Qg = Q_air
left = alpha
Vm = (Qg + Qf)/A
epsilon = Qg/((Co*Vm + v_ts)*A)
sqep = epsilon**(0.5)
beta = 1 - (0.67)*(R/L)*sqep 

vf = Qf/A 
Re = rho_water*vf*D/mu

f = 0.316/(Re**(0.25))

expr = f*(Vm*Vm)/(2.0*g*D)

right = (1.0-epsilon)*(1.0+((1.0-beta)*expr+beta*(1.0-epsilon)))

equation = sympy.Eq(left, right)

Q_water = sympy.solveset(equation, Qf)
print(Q_water)