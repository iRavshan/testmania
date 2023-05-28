from django.core.exceptions import ValidationError
from .models import CustomUser

def CheckConfirmationPassword(password1, password2):
    return password1 == password2

def CleanUsername(username):
    usernames = CustomUser.objects.values('username')
    return not (username in usernames)


