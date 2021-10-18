from django.http import response
from django.test import TestCase

# Create your tests here.
class HomeViewTest(TestCase):

    def test_home_page_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')