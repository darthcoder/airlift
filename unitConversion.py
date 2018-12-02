# Mindlessly converting without thinking
# not plotting here

import numpy as np

rho_air = 1.225
rho_water = 1000

air_mfr = np.loadtxt('./data/air_kph.txt')
air_mfr_sec = air_mfr / 3600
air_vfr = air_mfr_sec / rho_air
air_feet = air_vfr / 0.028

np.savetxt('./data/air_stenning.txt', air_feet)