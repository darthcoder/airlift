import numpy as np
import matplotlib.pyplot as plt

# Q_g_dash = np.loadtxt("./data/kim_g.txt")

# Q_l_dash1 = np.loadtxt("./data/kim_l_8mm_sub0_9.txt")
# Q_l_dash2 = np.loadtxt("./data/kim_l_11mm_sub0_9.txt")
# Q_l_dash3 = np.loadtxt("./data/kim_l_18mm_sub0_9.txt")
# Q_l_dash4 = np.loadtxt("./data/kim_l_24mm_sub0_9.txt")

# print(Q_g_dash)
# print(Q_l_dash1)
# print(Q_l_dash2)
# print(Q_l_dash3)
# print(Q_l_dash4)

# dig = plt.figure()
# dia = dig.add_subplot(111)
# dia.set_title("$Q_l\'$ vs $Q_g\'$ for various dia at submergence ratio 0.9")
# dia.set_xlabel("$Q_g\'$")
# dia.set_ylabel("$Q_l\'$")
# plt.yscale('log')
# dia.plot(Q_g_dash, Q_l_dash1, 'r-', label='D = 8mm')
# dia.plot(Q_g_dash, Q_l_dash2, 'b-', label='D = 11mm')
# dia.plot(Q_g_dash, Q_l_dash3, 'g-', label='D = 18mm')
# dia.plot(Q_g_dash, Q_l_dash4, 'y-', label='D = 24mm')

# plt.legend(loc='lower right')
# plt.show()

afr = np.loadtxt("./data/air_standard.txt")
wfr = np.loadtxt("./data/kim_water_standard.txt")
expt = np.loadtxt("./data/kassab_water_kph.txt")

print(len(afr))
print(len(wfr))
print(len(expt))
dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("Comparison of Kim's Model with Experimental Data")
dia.set_xlabel("Mass flow rate of Air in kgph")
dia.set_ylabel("Mass flow rate of Water in kgph")
dia.plot(afr, wfr, label="Kim's Model")
dia.plot(afr, expt[3:], 'ro', label="Experimental Data")
plt.legend(loc="upper left")
plt.show()
