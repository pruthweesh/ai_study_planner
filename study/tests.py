from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import CustomUser
from .models import Progress, Notification

class ProgressTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpass123',
            role='STUDENT'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.progress = Progress.objects.create(
            user=self.user,
            subject='Mathematics',
            completed=50
        )

    def test_create_progress(self):
        url = reverse('progress-list')
        data = {
            'subject': 'Science',
            'completed': 30
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Progress.objects.count(), 2)

class NotificationTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test2@example.com',
            username='testuser2',
            password='testpass123',
            role='STUDENT'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.notification = Notification.objects.create(
            user=self.user,
            title='Test Notification',
            message='This is a test',
            notification_type='PROGRESS'
        )

    def test_get_notifications(self):
        url = reverse('notification-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)