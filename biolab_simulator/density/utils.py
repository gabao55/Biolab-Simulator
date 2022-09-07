from telnetlib import GA
from typing import Dict

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

    # It is getting to complex numbers in the den
    density = atm_density*(num/den.real)

    return round(density, 3)

def chhetri_watts_predict(temperature: float, pressure: float) -> float:
    return round(1036+0.00423*pressure-0.643*temperature, 3)

def rackett_soave_predict(intensive_parameters: Dict, compounds: Dict) -> float:
    density = 0
    temperature = intensive_parameters['Temperature']
    reference_temperature = intensive_parameters['Reference temperature']
    reference_density = intensive_parameters['Reference density']

    for parameters in compounds.values():
        xi = parameters['composition']/100
        Tc = parameters['Tc']
        acentric_factor = parameters['acentric factor']
        Gama = (1-temperature/Tc)**(2/7) - (1-reference_temperature/Tc)**(2/7)
        Zra = 0.2908-0.099*acentric_factor+0.04*acentric_factor**2

        density += xi*reference_density/(Zra**Gama)
        
    return round(density, 3)