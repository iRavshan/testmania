from django.db import models
from uuid import uuid4
from account.models import CustomUser
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=60, null=False)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4())
    thumbnail = models.FileField(upload_to='blog/thumbnails', null=True)
    is_editors_choise = models.BooleanField(default=False)
    author = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300, null=False)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

