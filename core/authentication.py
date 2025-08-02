from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class EmailOrUsernameAuthBackend(ModelBackend):
    """
    Custom authentication backend that allows login with:
    - Email
    - Username
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Allow authentication via either username or email
            user = User.objects.get(
                Q(username__iexact=username) | 
                Q(email__iexact=username)
            )
            
            # Verify the password
            if user.check_password(password):
                return user
                
        except User.DoesNotExist:
            # No user found with given credentials
            return None
            
        except Exception as e:
            # Handle other potential errors
            print(f"Authentication error: {str(e)}")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None