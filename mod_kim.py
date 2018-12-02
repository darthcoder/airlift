#--------------------------------------------------------------------
# Using the colebrook equation model of friction factor here
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
# from math import pi
from functions import vm, right_hs
from scipy.optimize import root
# import sympy

# sympy.init_printing(use_unicode=True)

L = 3.75
g = 9.81
D = 0.0254
A = np.pi*(D**2)/4
alpha = 0.67
co =1.2
sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4

Bo = ((rho_water)*g*D**2/(sigma))
v_ts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))

air_kassab = np.loadtxt("./data/air_standard.txt")
Qg = np.zeros(len(air_kassab))
Qg = air_kassab / ( 3600 * rho_air )
Qg_dsh = Qg / (A*np.sqrt(g*D))

ndivi = 100000
Ql = np.array([])
Ql_dsh = np.array([])
Ql_try = np.linspace(0.01, 100, ndivi)


# f = sympy.symbols("f")
tempy = 0
for qg in Qg_dsh:
    for ql_dash in Ql_try:
        vm_dash = vm(ql_dash, qg)
        ql = ql_dash*A*np.sqrt(g*D)
        vl = ql/A
        qg_air = qg*A*np.sqrt(g*D)
        vg = qg_air / A
        vm1 = vl+vg
        Re = rho_air*vm1*D/mu
        # Re = rho_water*vl*D/mu
        # k = 0.2e-3
        def f_factor(x):
            return (-2*np.log10((2.51/(Re*np.sqrt(x)))) - 1.0/np.sqrt(x))

        f = root(f_factor, 0.001)["x"][-1]
        # print(f_factor)
        # left = sqrt(f)
        # right = 2*np.log(2.51/(Re*sqrt(f)))

        # the_equation = sympy.Eq(left, right)
        # sympy.solveset(the_equation,f)

        # f = (1.8*np.log(6.9/Re))**(-2)
        lhs = ql_dash
        rhs = right_hs(vm_dash, co, v_ts_dash, alpha, f)
        diff = abs(lhs - rhs)

        if (diff < 0.001):
            tempy = ql_dash
            # tempy = ql
            break
        
    Ql_dsh = np.append(Ql_dsh, tempy)
    # Ql = np.append(Ql, tempy)

factor = A * np.sqrt(g*D)
print(factor)
print(Ql_dsh)

Ql = Ql_dsh * factor
print(Ql)
W = Ql * rho_water * 3600 
# W = Ql * rho_water 
# W[0] = 4000
print(W)

np.savetxt("./data/kim_water_colebrook.txt", W)