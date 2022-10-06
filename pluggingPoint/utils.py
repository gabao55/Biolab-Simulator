from typing import Dict

def li_bing_predict(compounds: Dict) -> float:
    LSCF = 0

    for parameters in compounds.values():
        xi = parameters['composition']/100
        melting_point = parameters['Melting point']

        LSCF += xi*melting_point/100

    cffp = 1.7556*LSCF-14.772

    # It is getting to complex numbers in the den

    return round(cffp, 3)
