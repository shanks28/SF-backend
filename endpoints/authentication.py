from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailorPhone(ModelBackend):
    def authenticate(self, request,username=None,password=None,**kwargs):
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(Q(email__iexact=username)|Q(phone__iexact=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None