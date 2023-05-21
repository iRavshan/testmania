from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    study_center = models.TextField(default=None, null=True)
    avatar = models.ImageField(upload_to='avatars', default='avatars/default_user.png', null=True)