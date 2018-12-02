import numpy as np
import matplotlib.pyplot as plt

Qg_dash = np.loadtxt('./data/rei_g.txt')

# Ql_dash1 = np.loadtxt('./data/rei_l_3mm_sub0_6.txt')
Ql_dash2 = np.loadtxt('./data/rei_l_6mm_sub0_6.txt')
Ql_dash3 = np.loadtxt('./data/rei_l_9mm_sub0_6.txt')
Ql_dash4 = np.loadtxt('./data/rei_l_11mm_sub0_6.txt')
Ql_dash5 = np.loadtxt('./data/rei_l_19mm_sub0_6.txt')

dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("$Q_l\'$ vs $Q_g\'$ for various dia at submergence ratio 0.6")
dia.set_xlabel("$Q_g\'$")
dia.set_ylabel("$Q_l\'$")
# plt.yscale('log')
# dia.plot(Qg_dash, Ql_dash1, 'r-', label='D = 3mm')
dia.plot(Qg_dash, Ql_dash2, 'b-', label='D = 6mm')
dia.plot(Qg_dash, Ql_dash3, 'g-', label='D = 9mm')
dia.plot(Qg_dash, Ql_dash4, 'y-', label='D = 11mm')
dia.plot(Qg_dash, Ql_dash5, 'y-', label='D = 19mm')
plt.legend(loc='lower right')
plt.show()


#----------------------------------------------------------------------------------


# afr = np.loadtxt("./data/air_standard.txt")
# wfr = np.loadtxt("./data/reinemann_water_standard.txt")
# expt = np.loadtxt("./data/kassab_water_kph.txt")
# dig = plt.figure()
# dia = dig.add_subplot(111)
# dia.set_title("Comparison of Reinemann's Model with Experimental Data")
# dia.set_xlabel("Mass flow rate of Air in kgph")
# dia.set_ylabel("Mass flow rate of Water in kgph")
# dia.plot(afr, wfr, label="Reinemann's Model")
# dia.plot(afr, expt[3:], 'ro', label="Experimental Data")
# plt.legend(loc='lower left')
# plt.show()
