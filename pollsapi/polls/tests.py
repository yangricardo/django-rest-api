from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import views
from django.contrib.auth import get_user_model


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = self.setup_user()
        self.view = views.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
