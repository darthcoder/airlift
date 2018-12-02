# This program includes a simple function
# for converting mass flow of air and water
# in kgps to lpm

def kgps_to_lpm(kgps, density):
    """ vol_flow_rate_SI = 
            mass_flow_rate/density

        vol_flow_rate_lpm = 
            vol_flow_rate_SI * 60000
    """

    vfr_SI = kgps/density
    return vfr_SI*6e4


def lpm_to_kgps(lpm, density):
    """ vol_flow_rate_SI = lpm/(60000)

        mass_flow_rate = 
                vol_flow_rate_SI * density
    """

    vfr_SI = lpm/(6e4)
    return vfr_SI*density