from django.test import SimpleTestCase, TestCase
from ..utils import lapuerta_rodriguez_predict


class TestLapuertaRodriguezPredictiveModel(SimpleTestCase):
    def setUp(self) -> None:
        self.caprate_ethyl_esther_data = {
            "Esther parameter 1": "2",
            "Carbons number 1": "10",
            "Double bonds 1": "0",
            "Volume % 1": "100",
        }
        self.caprate_propyl_esther_data = {
            "Esther parameter 1": "3",
            "Carbons number 1": "10",
            "Double bonds 1": "0",
            "Volume % 1": "100",
        }
        self.caprate_butyl_esther_data = {
            "Esther parameter 1": "4",
            "Carbons number 1": "10",
            "Double bonds 1": "0",
            "Volume % 1": "100",
        }
        self.pamitate_ethyl_esther_data = {
            "Esther parameter 1": "2",
            "Carbons number 1": "16",
            "Double bonds 1": "0",
            "Volume % 1": "100",
        }
        self.palmitoleate_ethyl_esther_data = {
            "Esther parameter 1": "2",
            "Carbons number 1": "16",
            "Double bonds 1": "1",
            "Volume % 1": "100",
        }
        self.linoleate_ethyl_esther_data = {
            "Esther parameter 1": "2",
            "Carbons number 1": "18",
            "Double bonds 1": "2",
            "Volume % 1": "100",
        }

        self.caprate_ethyl_esther_cetane_number = 51.5
        self.caprate_propyl_esther_cetane_number = 54.4
        self.caprate_butyl_esther_cetane_number = 57.3
        self.pamitate_ethyl_esther_cetane_number = 81.9
        self.palmitoleate_ethyl_esther_cetane_number = 59.6
        self.linoleate_ethyl_esther_cetane_number = 44.9

        self.mixture_compounds = [
            self.linoleate_ethyl_esther_data,
            self.palmitoleate_ethyl_esther_data,
            self.pamitate_ethyl_esther_data,
            self.caprate_butyl_esther_data
        ]

        self.mixtured_esthers = {}

        for i in range(4):
            self.mixtured_esthers[f"Esther parameter {i+1}"] = self.mixture_compounds[i]["Esther parameter 1"]
            self.mixtured_esthers[f"Carbons number {i+1}"] = self.mixture_compounds[i]["Carbons number 1"]
            self.mixtured_esthers[f"Double bonds {i+1}"] = self.mixture_compounds[i]["Double bonds 1"]
            self.mixtured_esthers[f"Volume % {i+1}"] = 25
        
        self.mixtured_esthers_cetane_number = 60.9

    def test_single_esthers_cetane_numbers(self):
        predicted_caprate_ethyl_esther_cetane_number = lapuerta_rodriguez_predict(self.caprate_ethyl_esther_data)[0]
        predicted_caprate_propyl_esther_cetane_number = lapuerta_rodriguez_predict(self.caprate_propyl_esther_data)[0]
        predicted_caprate_butyl_esther_cetane_number = lapuerta_rodriguez_predict(self.caprate_butyl_esther_data)[0]
        predicted_palmitate_ethyl_esther_cetane_number = lapuerta_rodriguez_predict(self.pamitate_ethyl_esther_data)[0]
        predicted_palmitoleate_ethyl_esther_cetane_number = lapuerta_rodriguez_predict(self.palmitoleate_ethyl_esther_data)[0]
        predicted_linoleate_ethyl_esther_cetane_number = lapuerta_rodriguez_predict(self.linoleate_ethyl_esther_data)[0]

        self.assertEqual(predicted_caprate_ethyl_esther_cetane_number, self.caprate_ethyl_esther_cetane_number)
        self.assertEqual(predicted_caprate_propyl_esther_cetane_number, self.caprate_propyl_esther_cetane_number)
        self.assertEqual(predicted_caprate_butyl_esther_cetane_number, self.caprate_butyl_esther_cetane_number)
        self.assertEqual(predicted_palmitate_ethyl_esther_cetane_number, self.pamitate_ethyl_esther_cetane_number)
        self.assertEqual(predicted_palmitoleate_ethyl_esther_cetane_number, self.palmitoleate_ethyl_esther_cetane_number)
        self.assertEqual(predicted_linoleate_ethyl_esther_cetane_number, self.linoleate_ethyl_esther_cetane_number)

    def test_mixture_of_esthers_cetane_numbers(self):
        predicted_cetane_number = lapuerta_rodriguez_predict(self.mixtured_esthers)[0]

        self.assertEqual(predicted_cetane_number, self.mixtured_esthers_cetane_number)