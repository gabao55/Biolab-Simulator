from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import contact, Home


class TestUrlsHome(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home:home')
        self.assertEquals(resolve(url).func.view_class, Home)

    def test_contact_url_resolves(self):
        url = reverse('home:contact')
        self.assertEquals(resolve(url).func, contact)