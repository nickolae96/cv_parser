from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework.test import APIClient

from cv_api.serializers import CVSerializer

client = APIClient()

class SectionsTest(SimpleTestCase):

    def test_experience(self):
        url = reverse('experience')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) > 0

    def test_personal(self):
        url = reverse('personal')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) > 0

    def test_education(self):
        url = reverse('education')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) > 0
