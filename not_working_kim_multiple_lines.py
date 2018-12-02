
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt
from functions import vm, right_hs, key

L = 0.5
g = 9.81
#D = np.array([0.008, 0.011, 0.018, 0.024]
D = 0.008
D1 = 0.011
D2 = 0.018
D3 = 0.024

A = pi*D**2/4
A1 = pi*D1**2/4
A2 = pi*D2**2/4
A3 = pi*D3**2/4

alpha = 0.8
alpha1 = 0.9
#co = 1.2

sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4 #viscosity of water at 25 C in Pa.s

Bo = ((rho_water)*g*D**2/(sigma))
Bo1 = ((rho_water)*g*D1**2/(sigma))
Bo2 = ((rho_water)*g*D2**2/(sigma))
Bo3 = ((rho_water)*g*D3**2/(sigma))

v_ts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))
v_ts_dash1 = 0.352 * (1 - 3.18 * (Bo1 ** -1) - 14.77 * (Bo1 ** -2))
v_ts_dash2 = 0.352 * (1 - 3.18 * (Bo2 ** -1) - 14.77 * (Bo2 ** -2))
v_ts_dash3 = 0.352 * (1 - 3.18 * (Bo3 ** -1) - 14.77 * (Bo3 ** -2))

ndiv = 200
Q_g_dash = np.linspace(0.1, 10, ndiv)
Q_l_dash_try = np.linspace(0.01, 100, 10000)
# Q_l_dash = np.zeros(ndiv)
# Q_l_dash1 = np.zeros(ndiv)
# Q_l_dash2 = np.zeros(ndiv)
# Q_l_dash3 = np.zeros(ndiv)
Q_l_dash = np.array([])
Q_l_dash1 = np.array([])
Q_l_dash2 = np.array([])
Q_l_dash3 = np.array([])

#Qldash = np.empty(len(D))

temp = 0
temp1 = 0
temp2 = 0
temp3 = 0

for qgdash in Q_g_dash:
    for qldash in Q_l_dash_try:
        vm_dash = vm(qgdash,qldash)

        ql = qldash*A*sqrt(g*D)
        ql1 = qldash*A1*sqrt(g*D1)
        ql2 = qldash*A2*sqrt(g*D2)
        ql3 = qldash*A3*sqrt(g*D3)

        vl = ql/A
        vl1 = ql1/A1
        vl2 = ql2/A2
        vl3 = ql3/A3

        Re = rho_water*vl*D/mu
        Re1 = rho_water*vl1*D1/mu
        Re2 = rho_water*vl2*D2/mu
        Re3 = rho_water*vl3*D3/mu

        if (Re < 2300):
            co = 2
            f = 64/Re
            
        else:
            co = 1.2
            f = 0.316/(pow(Re, 0.25))

        if (Re1 < 2300):
            co1 = 2
            f1 = 64/Re1
            
        else:
            co1 = 1.2
            f1 = 0.316/(pow(Re1, 0.25))

        if (Re2 < 2300):
            co2 = 2
            f2 = 64/Re2
            
        else:
            co2 = 1.2
            f2 = 0.316/(pow(Re2, 0.25))

        if (Re3 < 2300):
            co3 = 2
            f3 = 64/Re3
            
        else:
            co3 = 1.2
            f3 = 0.316/(pow(Re3, 0.25))
        
        #k = key(f, vm_dash)
        #lhs = qldash * k
        lhs = qldash
        #rhs = k*vm_dash - (co*vm_dash + v_ts_dash)*(k-alpha)

        rhs = right_hs(vm_dash, co, v_ts_dash, alpha, f)
        rhs1 = right_hs(vm_dash, co1, v_ts_dash1, alpha, f1)
        rhs2 = right_hs(vm_dash, co2, v_ts_dash2, alpha, f2)
        rhs3 = right_hs(vm_dash, co3, v_ts_dash3, alpha, f3)

        diff = abs(lhs - rhs)
        diff1 = abs(lhs - rhs1)
        diff2 = abs(lhs - rhs2)
        diff3 = abs(lhs - rhs3)

        if (diff < 0.001):
            temp = qldash
            break

        if (diff1 < 0.001):
            temp1 = qldash
            break
        if (diff2 < 0.001):
            temp2 = qldash
            break

        if (diff3 < 0.001):
            temp3 = qldash
            break

    Q_l_dash = np.append(Q_l_dash, temp)
    Q_l_dash1 = np.append(Q_l_dash1, temp1)
    Q_l_dash2 = np.append(Q_l_dash2, temp2)
    Q_l_dash3 = np.append(Q_l_dash3, temp3)

# Q_l_dash = np.trim_zeros(Q_l_dash)
# Q_l_dash1 = np.trim_zeros(Q_l_dash1)
# Q_l_dash2 = np.trim_zeros(Q_l_dash2)
# Q_l_dash3 = np.trim_zeros(Q_l_dash3)

# print(len(Q_g_dash))
# print(len(Q_l_dash))
# print(len(Q_l_dash1))
# print(len(Q_l_dash2))
# print(len(Q_l_dash3))
#print(Q_l_dash)    

# plt.yscale('log')
# plt.xscale('log')
# plt.plot(Q_g_dash,Q_l_dash,'ro', label='$Q_l\'$ vs $Q_g\'$')
# plt.show()

dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("$Q_l\'$ as a function of $Q_g\'$ for submergence ratio = 0.8")
dia.set_xlabel("$Q_g\'$")
dia.set_ylabel("$Q_l\'$")
dia.plot(Q_g_dash, Q_l_dash, 'r+', label= '8mm dia')
dia.plot(Q_g_dash, Q_l_dash1, 'b+', label='11mm dia')
dia.plot(Q_g_dash, Q_l_dash2, 'g+', label='18mm dia')
dia.plot(Q_g_dash, Q_l_dash3, 'y+', label='24mm dia')

plt.legend(loc='lower right')
plt.show()