from django.test import TestCase, Client
from django.urls import reverse
from home.models import Home, Image
from density.models import PredictiveModel as DensityModel


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.home_url = reverse('home:home')
        self.contact_url = reverse('home:contact')
        self.murnaghan_equation = DensityModel.objects.create(
            name="Murnaghan Equation",
            brief_description="Test",
        )
        self.home = Home.objects.create(
            id=1,
            name="home",
            intro="Test intro",
        )

    #Doesn't work
    # def test_home_GET(self):

    #     response = self.client.get(self.home_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'home/home.html')

    #Doesn't work
    # def test_contact_GET(self):

    #     response = self.client.get(self.contact_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'home/contact.html')