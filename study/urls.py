from django.urls import path
from .views import (
    ProgressListView,
    NotificationListView,
    test_api,
)
from django.http import JsonResponse

urlpatterns = [
    path('', lambda request: JsonResponse({'message': 'Welcome to AI Study Planner API'})),
    
    # User endpoints
    path('api/notifications/', NotificationListView.as_view(), name='notifications'),
    path('api/progress/', ProgressListView.as_view(), name='progress'),
    
    # Test endpoint
    path('api/test/', test_api),
    
    # Admin endpoints (secured via IsAdminUser)
    path('api/admin/notifications/', notification_list),
    path('api/admin/progress/', progress_list),
]