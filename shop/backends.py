from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class UserEmailBackend:

    def authenticate(self, request, username=None, password=None):

        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except user_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None