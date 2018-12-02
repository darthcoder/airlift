# Esen's formula:
# Q_f/(A.sqrt(2gL)) = c + m.log_(10)(Q_g/A.sqrt(2gL))
#
# H/L           c               m
# 0.226         0.0438          0.228
# 0.339         0.0746          0.237
# 0.452         0.1110          0.250
# 0.565         0.1517          0.226
# 0.678         0.1968          0.186
# 0.791         0.2420          0.160


import numpy as np
import matplotlib.pyplot as plt
import flowrate as fr
from math import pi

#all qtys in SI unless mentioned

g = 9.81
# L = 0.54
# A = 20*80*1e-6
L = 3.75
D = 0.0254
A = pi * (D**2) / 4
rho_air = 1.225
rho_water = 1000.0

air_flow_rate = np.linspace(0.004,0.025,100)
air_from_expt = np.loadtxt("./data/kassab_air_kph.txt")

Q_g = air_flow_rate/(rho_air)
Q_g_lpm = fr.kgps_to_lpm(air_flow_rate,rho_air)


submergence_ratio = np.array([0.226, 0.339, 0.452,
                    0.565, 0.678, 0.791])

c = np.array([0.0438, 0.0746, 0.1110, 0.1517,
            0.1968, 0.2420])

m = np.array([0.228, 0.237, 0.250, 0.226,
            0.186, 0.160])

Q_l = np.zeros((len(m),len(Q_g)),dtype=float)

def gen_function(q_g, L, A, c, m, g):
    return A*(np.sqrt(2*g*L))*(c+m*np.log10(q_g/(A*(np.sqrt(2*g*L)))))

for i in np.arange(len(m)):
    Q_l[i,:] = gen_function(Q_g,L,A,c[i],m[i],g)
    # this Q_l is in cubic meter per second
#    print(Q_l[i,:])
Q_l_lpm = Q_l*6e4
Q_l_mfr = fr.lpm_to_kgps(Q_l_lpm,rho_water)

#print(Q_l)
#print(np.arange(len(m)))
#Q_l_lpm = kgps_to_lpm(Q_l, rho_water)

E = np.zeros((len(m),len(Q_g)),dtype=float)

for i in np.arange(len(m)):
    E[i] = Q_l_mfr[i,:]/air_flow_rate


#------------------ Plot the E (effectiveness) vs Q_g ----------------------
# dig = plt.figure()
# dia = dig.add_subplot(111)
# dia.set_title("Effectiveness as a function of air flow rate")
# dia.set_xlabel("$Q_g$")
# dia.set_ylabel("$E$")
# dia.plot(air_flow_rate,E[0],'ro', label='s = 0.226')
# dia.plot(air_flow_rate,E[1],'bo', label='s = 0.339')
# dia.plot(air_flow_rate,E[2],'go', label='s = 0.452')
# dia.plot(air_flow_rate,E[3],'r+', label='s = 0.565')
# dia.plot(air_flow_rate,E[4],'b+', label='s = 0.678')
# dia.plot(air_flow_rate,E[5],'g+', label='s = 0.751')
# plt.legend(loc='upper right')
#---------------------------------------------------------------------------


#------------------- Plot the Q_l vs Q_g -----------------------------------
# dig = plt.figure()
# dia = dig.add_subplot(111)
# dia.set_title("$Q_l$ vs $Q_g$ for various s")
# dia.set_xlabel("$Q_g$")
# dia.set_ylabel("$Q_l$")
# plt.yscale('log')
# dia.plot(Q_g, Q_l[0,:], 'ro', label='s = 0.226')
# dia.plot(Q_g, Q_l[1,:], 'bo', label='s = 0.339')
# dia.plot(Q_g, Q_l[2,:], 'go', label='s = 0.452')
# dia.plot(Q_g, Q_l[3,:], 'r+', label='s = 0.565')
# dia.plot(Q_g, Q_l[4,:], 'b+', label='s = 0.678')
# dia.plot(Q_g, Q_l[5,:], 'g+', label='s = 0.751')
# plt.legend(loc='lower right')
#---------------------------------------------------------------------------
# plt.show()

# air_from_expt is in kgph 
# need to convert to cubic meter per second
# Qgh(cubic meter per hour) = (air_from_expt / rho_air)
# Qg(cubic meter per second) = Qgh /3600
Qg = air_from_expt/(rho_air * 3600) # to convert to cubic meter per second
Ql = np.zeros(len(Qg))

# Q_l[i,:] = gen_function(Q_g,L,A,c[i],m[i],g)

Ql = gen_function(Qg, L, A, c[4], m[4], g)

water_mass_flow_rate_kps = Ql * rho_water
water_mass_flow_rate_kph = water_mass_flow_rate_kps * 3600
water_kassab = np.loadtxt("./data/kassab_water_kph.txt")
# print(water_mass_flow_rate_kph)
# print(air_from_expt)
air_from_expt_sanitized = air_from_expt[3:]
water_mass_flow_rate_kph_sanitized = water_mass_flow_rate_kph[3:]
water_kim = np.loadtxt("./data/kim_water_standard.txt")[3:]
water_kim_colebrook = np.loadtxt("./data/kim_water_colebrook.txt")
water_rei = np.loadtxt("./data/rei_new.txt")
water_sten = np.loadtxt("./data/stenning_water_standard.txt")
water_theory = np.loadtxt("./data/mashup_mod.txt")
water_true = np.loadtxt("./data/true_modified.txt")
water_new_per_bubble = np.loadtxt("./data/new_per_bubble.txt")
# water_kim_new = np.loadtxt("./data/kim_new_water_standard.txt")
# water_kim_new_sanitized = water_kim_new[3:]
# print(len(water_kim))
# print(len(water_kim_new))
# print(len(water_kim_new_sanitized))
# np.savetxt("./data/esen_water")
# print(Ql)
# plt.plot(Qg, Ql)
# plt.plot(air_from_expt_sanitized, water_mass_flow_rate_kph_sanitized)
# plt.plot(air_from_expt_sanitized, water_kassab[3:], 'ro')
# plt.show()

# np.savetxt("./data/air_standard.txt", air_from_expt_sanitized)
# np.savetxt("./data/esen_water_standard.txt", water_mass_flow_rate_kph_sanitized)

dig = plt.figure()
dia = dig.add_subplot(111)
dia.set_title("Comparison of Theoretical Models with Experimental Data")
dia.set_xlabel("Mass flow rate of air in kgph ")
dia.set_ylabel("Mass flow rate of water in kgph ")
# plt.yscale('log')
dia.plot(air_from_expt_sanitized, water_mass_flow_rate_kph_sanitized, 
        label='Esen Theory')

plt.plot(air_from_expt_sanitized, water_kim, label="Kim Theory")
plt.plot(air_from_expt_sanitized, water_rei, label="Reinemann Theory")
plt.plot(air_from_expt_sanitized, water_sten, label="Stenning Theory")
plt.plot(air_from_expt_sanitized, water_theory, 'r--', label="Unit Cell Approach")
plt.plot(air_from_expt_sanitized, water_new_per_bubble, 'b--', label="Per Bubble Approach")
# plt.plot(air_from_expt_sanitized, water_true, 'b--', label="Per Bubble Approach")
# plt.plot(air_from_expt_sanitized, water_theory, label= "Current Theory")
# plt.plot(air_from_expt_sanitized, water_kim_new_sanitized, 'y*', label="Kim New")

plt.plot(air_from_expt_sanitized, water_kassab[3:], 'ro', label='Experiment')
plt.legend(loc='upper left')
plt.show()