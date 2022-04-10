from typing import Dict, Any

def murnaghan_equation_predict(intensive_parameters: Dict, compounds: Dict) -> float:
    num = 0
    den = 0
    temperature = intensive_parameters['Temperature']
    pressure = intensive_parameters['Pressure']
    atm_density = intensive_parameters['Atmospheric density']

    for parameters in compounds.values():
        xi = parameters['composition']/100
        a0 = parameters['a0']
        a1 = parameters['a1']
        a2 = parameters['a2']
        b0 = parameters['b0']
        b1 = parameters['b1']
        b2 = parameters['b2']
        c0 = parameters['c0']
        c1 = parameters['c1']

        Ai = a0 + a1*temperature + a2*temperature**2
        Bi = b0 + b1*temperature + b2*temperature**2
        Ci = c0 + c1*temperature
        num += xi*Ai
        den += xi*Ai*(1 + Bi*pressure)**Ci

    density = atm_density*(num/den)

    return round(density, 3)