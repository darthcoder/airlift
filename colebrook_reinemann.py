# This uses the Colebrook eqn for modeling friction factor
# with the Reinemann's equation. Rest everything is pretty
# much the same as before. Hopefully, it will be more accurate

import numpy as np
import matplotlib.pyplot as plt
import math
from functions import epsilon

L = 3.75
g = 9.81
#D = varies from 3.18 to 19.1 mm incl. 6.35 and 9.53
D = 0.0254
A = math.pi*D**2/4
alpha = 0.67

co = 1.2 # only one formula is used in this paper
sigma = 7.28e-2
rho_water = 1000
rho_air = 1.225
mu = 8.9e-4 #viscosity of water at 25 C in Pa.s

Bo = ((rho_water)*g*D**2/(sigma))
vts_dash = 0.352 * (1 - 3.18 * (Bo ** -1) - 14.77 * (Bo ** -2))

def ff(Re):
    f_try = np.linspace(0.0000001, 10, 10000000)
    f = 0

    for fin in f_try:
        lhs = 1 / (math.sqrt(fin))
        x = 2.51/(Re*math.sqrt(fin))
        rhs = (-2.0) * math.log(x)

        diff = abs(lhs - rhs)

        if (diff < 0.001):
            f = fin
            print("hit")
            break
    
    return f

print(ff(100))

