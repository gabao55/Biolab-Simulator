from django.test import SimpleTestCase
from ..utils import murnaghan_equation_predict


class TestMurnaghanEquation(SimpleTestCase):
    def setUp(self):
        self.intensive_parameters = {'Temperature': 308.15, 'Pressure': 2.00, 'Atmospheric density': 872.2}
        self.single_esther_composition = {'FAME C10:0': {'composition': 100.0, 'a0': 167.8959, 'a1': 0.1067739, 'a2': 0.000166961, 'b0': 0.0167704, 'b1': -0.00010389, 'b2': 2.5e-07, 'c0': -0.092921, 'c1': -3.74e-05}}
        self.mixture_composition = {'FAME C10:0': {'composition': 34.0, 'a0': 167.8959, 'a1': 0.1067739, 'a2': 0.000166961, 'b0': 0.0167704, 'b1': -0.00010389, 'b2': 2.5e-07, 'c0': -0.092921, 'c1': -3.74e-05}, 'FAEE C20:1': {'composition': 33.0, 'a0': 320.6425, 'a1': 0.1416488, 'a2': 0.000315043, 'b0': 0.003820384, 'b1': -1.52e-07, 'b2': 6.68e-08, 'c0': -0.1112576, 'c1': -3.31e-05}, 'Glyceride Di': {'composition': 33.0, 'a0': 344.7225, 'a1': 0.1698488, 'a2': 0.000315043, 'b0': 0.003930681, 'b1': -1.61e-06, 'b2': 6.45e-08, 'c0': -0.1227918, 'c1': -6.36e-06}}

        self.single_esther_density = 873.731
        self.mixture_density = 874.172
                
    def single_esther_test_with_mocked_data(self):
        predicted_density = murnaghan_equation_predict(self.intensive_parameters, self.single_esther_composition)

        self.assertEqual(predicted_density, self.single_esther_density)

    def mixture_test_with_mocked_data(self):
        predicted_density = murnaghan_equation_predict(self.intensive_parameters, self.mixture_composition)

        self.assertEqual(predicted_density, self.mixture_density)