from django.test import SimpleTestCase

from ..utils import su_liu_predict


class TestSuLiuCorrelation(SimpleTestCase):
    def setUp(self) -> None:
        self.canola_oil_data = {
            "Content of unsaturated": "91.80",
            "Carbon atoms": "17.83",
        }
        self.copra_oil_data = {
            "Content of unsaturated": "7.10",
            "Carbon atoms": "12.54",
        }
        self.pequi_oil_data = {
            "Content of unsaturated": "54.96",
            "Carbon atoms": "16.21",
        }
        self.groundnut_oil_data = {
            "Content of unsaturated": "81.58",
            "Carbon atoms": "18.04",
        }
        self.palm_oil_data = {
            "Content of unsaturated": "53.68",
            "Carbon atoms": "16.99",
        }

        self.canola_oil_cffp = -25.68
        self.copra_oil_cffp = -52.90
        self.pequi_oil_cffp = -25.25
        self.groundnut_oil_cffp = -13.68
        self.palm_oil_cffp = -10.17

    def test_oils_cffp(self):
        predicted_canola_oil_cffp = su_liu_predict(self.canola_oil_data)
        predicted_copra_oil_cffp = su_liu_predict(self.copra_oil_data)
        predicted_pequi_oil_cffp = su_liu_predict(self.pequi_oil_data)
        predicted_groundnut_oil_cffp = su_liu_predict(self.groundnut_oil_data)
        predicted_palm_oil_cffp = su_liu_predict(self.palm_oil_data)

        self.assertEqual(predicted_canola_oil_cffp, self.canola_oil_cffp)
        self.assertEqual(predicted_copra_oil_cffp, self.copra_oil_cffp)
        self.assertEqual(predicted_pequi_oil_cffp, self.pequi_oil_cffp)
        self.assertEqual(predicted_groundnut_oil_cffp, self.groundnut_oil_cffp)
        self.assertEqual(predicted_palm_oil_cffp, self.palm_oil_cffp)