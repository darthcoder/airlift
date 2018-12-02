import numpy as np
import matplotlib.pyplot as plt

water_theory = np.loadtxt("./data/mashup_mod.txt")
air_from_expt = np.loadtxt("./data/kassab_air_kph.txt")
water_kassab = np.loadtxt("./data/kassab_water_kph.txt")

air_from_expt_sanitized = air_from_expt[3:]

dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("Plot of the Unit Cell Model")
dia.set_xlabel("Mass flow rate of air in kgph ")
dia.set_ylabel("Mass flow rate of water in kgph ")

plt.plot(air_from_expt_sanitized, water_theory, label="Unit Cell Approach")
plt.plot(air_from_expt_sanitized, water_kassab[3:], 'ro', label='Experiment')
plt.legend(loc='upper left')
plt.show()
