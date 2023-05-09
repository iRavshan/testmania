from django.db import models
from uuid import uuid4
from account.models import CustomUser
from ckeditor.fields import RichTextField

class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4())
    thumbnail = models.FileField(upload_to='blog/thumbnails', null=True)
    author = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300, null=False)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
