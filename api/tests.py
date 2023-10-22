from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserSetting


class UserSettingAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_user_setting(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'expected_calories_per_day': 2600
        }
        response = self.client.post('http://127.0.0.1:8000/user/set_calorie', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CalorieEntryAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Add User settting object
        UserSetting.objects.create(user=self.user, expected_calories_per_day=2000)


    def test_create_calorie_entry(self):
        # self.test_create_user_setting()
        self.client.force_authenticate(user=self.user)
        data = {
            'text': 'Oats breakfast',
            'calories': 400,
        }
        response = self.client.post('http://127.0.0.1:8000/user/entry', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_view_calorie_entry(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('http://127.0.0.1:8000/user/view_entry', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_calorie_entry_with_negative_calories(self):
        self.client.force_authenticate(user=self.user)

        # Attempt to create a CalorieEntry with negative calories
        calorie_entry_data = {
            'text': 'Lunch',
            'calories': -100
        }
        response = self.client.post('http://127.0.0.1:8000/user/entry', calorie_entry_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_view_calorie_entry_detail(self):
        self.client.force_authenticate(user=self.user)
        self.test_create_calorie_entry()
        response = self.client.get('http://127.0.0.1:8000/user/entry/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_calorie_entry(self):
        self.client.force_authenticate(user=self.user)
        self.test_create_calorie_entry()
        response = self.client.delete('http://127.0.0.1:8000/user/entry/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_update_calorie_entry(self):
        self.client.force_authenticate(user=self.user)
        self.test_create_calorie_entry()
        calorie_entry_data = {
            'text': 'Rice',
            'calories': 500
        }
        response = self.client.put('http://127.0.0.1:8000/user/entry_update/1', calorie_entry_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SetUserManagerAPITests(APITestCase):
    def setUp(self):
        # id : 1
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword')
        # id : 2
        self.user = User.objects.create_user(username='testuser', password='testpassword')


    def test_set_user_manager_without_admin(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'is_staff': 1
        }

        response = self.client.put('http://127.0.0.1:8000/user/set_usermanager/2', data, format='json')
        # user1 should not able to set testuser to usermanager
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserManagerAPITests(APITestCase):
    def setUp(self):
        self.usermanager = User.objects.create_user(username='testuser', password='testpassword')
        # set user manager
        self.usermanager.is_staff = True
        self.usermanager.save()

        # id: 2
        self.user = User.objects.create_user(username='user', password='testpassword')
    

    def test_usermanager_view(self):
        self.client.force_authenticate(user=self.usermanager)

        response = self.client.get('http://127.0.0.1:8000/users', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_usermanager_detail_view(self):
        self.client.force_authenticate(user=self.usermanager)

        response = self.client.get('http://127.0.0.1:8000/user/2', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_usermanager_delete_user(self):
        self.client.force_authenticate(user=self.usermanager)

        response = self.client.delete('http://127.0.0.1:8000/user/2', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)