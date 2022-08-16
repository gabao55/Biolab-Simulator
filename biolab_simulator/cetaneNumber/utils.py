def lapuerta_rodriguez_predict(data):
    number_of_compounds = int(len(data)/4)

    volumes = []
    cetane_numbers = []

    for i in range(number_of_compounds):
        esther_parameter = int(data[f"Esther parameter {i+1}"])
        carbons_number = int(data[f"Carbons number {i+1}"])
        number_of_double_bonds = int(data[f"Double bonds {i+1}"])
        volume_percentage = int(data[f"Volume % {i+1}"])

        A_parameter = -21.157 + 6.13*(esther_parameter - 1)
        B_parameter = 7.965 - 0.324*(esther_parameter - 1)
        C_parameter = -1.785 + 0.263*(esther_parameter - 1)
        D_parameter = 0.235 - 0.107*(esther_parameter - 1)
        E_parameter = -0.099

        cetane_number = A_parameter + (B_parameter + C_parameter*number_of_double_bonds + D_parameter*number_of_double_bonds**2)*carbons_number + E_parameter*carbons_number**2

        cetane_numbers.append(cetane_number)
        volumes.append(volume_percentage)

    volumes = [(lambda x: x/100)(x) for x in volumes]
    
    return round(volume_mixing_rule(volumes, cetane_numbers), 1), volumes

def volume_mixing_rule(volumes, cetane_numbers):
    resultado = 0
    for i in range(len(volumes)):
        resultado += volumes[i]*cetane_numbers[i]

    return resultado

def mass_mixing_rule(masses, cetane_numbers):
    resultado = 0
    for i in range(len(masses)):
        resultado += masses[i]*cetane_numbers[i]

    return resultado
