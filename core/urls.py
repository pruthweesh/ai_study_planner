from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CustomAuthToken,
    SignupView,
    LoginView,
    current_user,
    test_api
)

urlpatterns = [
    # Token Authentication
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    
    # Custom Auth Endpoints
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    
    # User Endpoints
    path('user/', current_user, name='current_user'),
    
    # Test Endpoint
    path('test/', test_api, name='test_api'),
]