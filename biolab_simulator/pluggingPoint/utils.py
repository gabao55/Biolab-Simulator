from typing import Dict

def su_liu_predict(data):
    unsaturated = float(data["Content of unsaturated"])
    carbon_atoms = float(data["Carbon atoms"])

    return round(18.019*carbon_atoms - 0.804*unsaturated - 273.15, 2)

def sarin_predict(data):
    PFAME = float(data["PFAME %"])

    return round(0.511*PFAME-7.823, 2)

def li_bing_predict(compounds: Dict) -> float:
    LSCF = 0

    for parameters in compounds.values():
        xi = parameters['composition']/100
        melting_point = parameters['Melting point']

        LSCF += xi*melting_point/100

    cffp = 1.7556*LSCF-14.772

    # It is getting to complex numbers in the den

    return round(cffp, 3)
