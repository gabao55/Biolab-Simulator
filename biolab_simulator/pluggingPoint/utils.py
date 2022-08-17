def su_liu_predict(data):
    unsaturated = float(data["Content of unsaturated"])
    carbon_atoms = float(data["Carbon atoms"])

    return round(18.019*carbon_atoms - 0.804*unsaturated - 273.15, 2)