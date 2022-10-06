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

def molecular_structure_predict(data):
    number_of_compounds = int(len(data)/4)

    molar_fractions = []
    densities = []

    for i in range(number_of_compounds):
        esther_parameter = int(data[f"Esther parameter {i+1}"])
        carbons_number = int(data[f"Carbons number {i+1}"])
        number_of_double_bonds = int(data[f"Double bonds {i+1}"])
        molar_fraction = int(data[f"Molar fraction {i+1}"])

        density = 851.471 + (250.718*number_of_double_bonds + 280.899 - 92.18*(esther_parameter - 1)) / (1.214 + carbons_number)

        densities.append(density)
        molar_fractions.append(molar_fraction)

    molar_fractions = [(lambda x: x/100)(x) for x in molar_fractions]
    
    return round(molar_mixing_rule(molar_fractions, densities), 1), molar_fractions

def molar_mixing_rule(fractions, densities):
    result = 0
    for i in range(len(fractions)):
        result += fractions[i]*densities[i]

    return result