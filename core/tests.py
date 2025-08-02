# backend/core/tests/test_auth.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import CustomUser
from rest_framework.authtoken.models import Token

class AuthTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')
        self.login_url = reverse('api_token_auth')
        
        # Create test users
        self.teacher = CustomUser.objects.create_user(
            username='testteacher',
            email='teacher@test.com',
            password='testpass123',
            role='TEACHER'
        )
        self.student = CustomUser.objects.create_user(
            username='teststudent',
            email='student@test.com',
            password='testpass123',
            role='STUDENT'
        )

    def test_student_signup(self):
        """Test student registration flow"""
        data = {
            'username': 'newstudent',
            'email': 'newstudent@test.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'role': 'STUDENT',
            'first_name': 'Test',
            'last_name': 'Student'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)
        
        # Verify user was created
        self.assertTrue(CustomUser.objects.filter(email='newstudent@test.com').exists())

    def test_teacher_login(self):
        """Test teacher login flow"""
        data = {
            'username': 'testteacher',
            'password': 'testpass123'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        
        # Verify token works
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        profile_response = self.client.get(reverse('current_user'))
        self.assertEqual(profile_response.status_code, status.HTTP_200_OK)

    def test_invalid_login(self):
        """Test failed login attempt"""
        data = {
            'username': 'testteacher',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)