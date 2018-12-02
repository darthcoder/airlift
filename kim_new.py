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



air_kassab = np.loadtxt("./data/kassab_air_kph.txt")
Qg = np.zeros(len(air_kassab))
Qg = air_kassab / ( 3600 * rho_air )
Qg_dsh = Qg / (A*sqrt(g*D))

# print(Qg_dsh)
ndivi = 100000
# Ql_dsh = np.array([])
Ql = np.array([])
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
            # tempy = ql_dash
            tempy = ql
            break
        
    # Ql_dsh = np.append(Ql_dsh, tempy)
    Ql = np.append(Ql, tempy)

# factor = A * sqrt(g*D)

# print(Ql_dsh)
# Ql = Ql_dsh * factor
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

np.savetxt("./data/kim_water_standard.txt", W)