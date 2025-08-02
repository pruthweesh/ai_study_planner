from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.permissions import BasePermission
from .models import Progress, Notification
from rest_framework.pagination import PageNumberPagination
from .serializers import ProgressSerializer, NotificationSerializer

# Secured debug endpoints (admin-only)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def notification_list(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def progress_list(request):
    progress = Progress.objects.all()
    serializer = ProgressSerializer(progress, many=True)
    return Response(serializer.data)

# Main user endpoints
class ProgressListView(generics.ListAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    page_size = 20

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

def test_api(request):
    return JsonResponse({"message": "API working fine"})
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'TEACHER'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'STUDENT'

class IsParent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'PARENT'