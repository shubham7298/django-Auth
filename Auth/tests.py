from django.test import TestCase, Client
from django.urls import reverse
from .models import UserInfo
from .forms import UserInfoForm
from django.contrib.auth.hashers import make_password


class FormTesting(TestCase):

    def test_registration_form(self):
        # test invalid data
        wrong_data = {
            'name': 'person1',
            'email': 'person1test.com',
            'password': 'password1'
        }
        form = UserInfoForm(data=wrong_data)
        form.is_valid()
        self.assertTrue(form.errors)

        # testing valid data
        right_data = {
            'name': 'person1',
            'email': 'person1@test.com',
            'password': 'password1'
        }
        form = UserInfoForm(data=right_data)
        form.is_valid()
        self.assertFalse(form.errors)


# Testing views

# testing registration view
class TestingRegistration(TestCase):

    def setUp(self):
        self.client = Client()

    def test_registration(self):
        url = reverse('register')

        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # test req method GET
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 203)
        # print(response)

        # testing valid data
        data = {
            'email': 'any@test.user',
            'password': 'lol',
            'name': 'ram',
        }
        response = self.client.post(url, data)
        # data gets inserted in db
        self.assertEqual(response.status_code, 201)

        # testing invalid data
        wrong_data = {
            'email': 'anytest.user',
            'password': 'lol',
            'name': 'ram',
        }
        response = self.client.post(url, wrong_data)
        self.assertEqual(response.status_code, 203)

# testing login view


class TestingLogin(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login(self):
        url = reverse('oauth')
        url_register = reverse('register')

        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # test req method POST
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 203)

        # logging with wrong data
        wrong_data = {
            'email': 'any@test.user',
            'password': 'lol',
        }
        response = self.client.post(url, wrong_data)
        # error
        self.assertEqual(response.status_code, 203)

        # to test login with right data
        # first we need to register
        data = {
            'email': 'any@test.user',
            'password': 'lol',
            'name': 'ram',
        }
        response = self.client.post(url_register, data)
        self.assertEqual(response.status_code, 201)
        # registration successful
        # Now, let's login
        right_data = {
            'email': 'any@test.user',
            'password': 'lol',
        }
        response = self.client.post(url, right_data)
        self.assertEqual(response.status_code, 200)
        # login successful

# testing home


class TestingHome(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home(self):
        url = reverse('home')

        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 501)

        # testing with invalid token
        header = {'HTTP_AUTHORIZATION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTgsImVtYWlsIjoid0BxLndxIn0.f9_nC7KDY-PBFPyTkzYFw9ReuVDE6MOXnRNY_NQj3Z8'}
        response = self.client.get(url, **header)
        self.assertEqual(response.status_code, 500)

        # For testing with valid token
        # We need to register first and then login
        # from login we will get authorization token(valid)
        url_register = reverse('register')
        url_login = reverse('oauth')
        # register
        data = {
            'email': 'any@test.user',
            'password': 'lol',
            'name': 'ram',
        }
        response = self.client.post(url_register, data)
        self.assertEqual(response.status_code, 201)
        # login
        right_data = {
            'email': 'any@test.user',
            'password': 'lol',
        }
        response = self.client.post(url_login, right_data)
        self.assertEqual(response.status_code, 200)
        # login successful, received token
        token = response.json()['token']
        print(token)
        # testing with valid token
        header = {'HTTP_AUTHORIZATION': token}
        response = self.client.get(url, **header)
        self.assertEqual(response.status_code, 200)
