import numpy as np
import matplotlib.pyplot as plt

# Qg = np.loadtxt('./data/stenning_air.txt')

# print(Qg)

# Ql1 = np.loadtxt('./data/stenning_water_s0_532.txt')
# Ql2 = np.loadtxt('./data/stenning_water_s0_629.txt')
# Ql3 = np.loadtxt('./data/stenning_water_s0_707.txt')

# dig = plt.figure()
# dia = dig.add_subplot(111)
# dia.set_title("$Q_l$ vs $Q_g$ for various submergence ratio")
# dia.set_xlabel("$Q_g$")
# dia.set_ylabel("$Q_l$")
# # plt.yscale('log')
# dia.plot(Qg, Ql1, 'r-', label='s = 0.532')
# dia.plot(Qg, Ql2, 'g-', label='s = 0.629')
# dia.plot(Qg, Ql3, 'b-', label='s = 0.707')

# plt.legend(loc='upper right')
# plt.show()

afr = np.loadtxt("./data/air_standard.txt")
wfr = np.loadtxt("./data/stenning_water_standard.txt")
expt = np.loadtxt("./data/kassab_water_kph.txt")

dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("Comparison of Stenning's Model with Experimental Data")
dia.set_xlabel("Mass flow rate of Air in kgph")
dia.set_ylabel("Mass flow rate of Water in kgph")
dia.plot(afr, wfr, label="Stenning's Model")
dia.plot(afr, expt[3:], 'ro', label="Experimental Data")
plt.legend(loc="lower right")
plt.show()