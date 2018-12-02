import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt


#---------------- Funtions required by kim.py ------------------------------

def vm(ql_ash, qg_dash):
    return  ql_ash + qg_dash

def right_hs(vm1, co, vts_dash, alph, fri):
    # return (vm1) - ((co*vm1)*vts_dash)*(1 - (alph/(1 + 0.5*fri*(vm1**2))))
    return (vm1) - ((co*vm1)*vts_dash)*(1 - (alph/(key(fri,vm1))))

def key(f, vmdash):
    return 1 + 0.5*f*(vmdash**2)
    
#---------------------------------------------------------------------------



#------------------Functions required by reinemann.py ----------------------

def epsilon(q_l, q_g, vtsdash):
    return q_g/(1.2*(q_l+q_g)+vtsdash)

def righths(ql1, qg1, e1, f1):
    return (1-e1)*(1 + (f1/2)*(ql1+qg1)**2)    

    

#---------------------------------------------------------------------------


#---------------------Functions required by stenning.py --------------------

def sfactor(qg, ql, g, d, v1):
    return ( 1.2 + 0.2 * (qg/ql) + 0.35 * (sqrt(g*d))/(v1) )   

def lefths(ar, s, qg, ql):
    return ( ar - (1/(1+(qg/(s*ql)))) )

def righthandside(vwater, gearth, Length, kfactor, qgrate, qlrate):
    return ((vwater**2)/(2*gearth*Length))*[(kfactor + 1) \
            + (kfactor + 2)*(qgrate/qlrate)]
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
