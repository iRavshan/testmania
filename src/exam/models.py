from django.db import models
from account.models import CustomUser
import uuid

class Test(models.Model):
    class Language(models.TextChoices):
        UZ = "o'zbek",
        RU = "rus",
        ENG = 'ingliz',
        KAR = 'qoraqalpoq'

    class Level(models.TextChoices):
        EASY = "oson",
        MEDIUM = "o'rta",
        HARD = "qiyin"

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    count_of_questions = models.PositiveIntegerField()
    count_of_subjects = models.PositiveIntegerField(default=1)
    desc = models.TextField()
    answers = models.CharField(max_length=95)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    file_of_questions = models.FileField(upload_to='questions/', null=False, default=None)
    language = models.TextField(choices=Language.choices, default=Language.UZ)
    level = models.TextField(choices=Level.choices, default=Level.MEDIUM)
    point = models.FloatField(default=1)

    def __str__(self) -> str:
        return self.name
    
    def __get_answers__(self) -> str:
        return self.answers

class TestScore(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True)
    count_of_questions = models.PositiveIntegerField(default=0)
    count_of_correct_answers = models.PositiveIntegerField(default=0)
    result = models.FloatField(default=0, null=True)

    def __str__(self) -> str:
        return str(self.count_of_correct_answers * self.test.point)


