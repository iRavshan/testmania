# Generated by Django 4.2 on 2023-05-09 12:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_editors_choise',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5389cf13-527e-448e-a787-59c3d9c64b1a'), primary_key=True, serialize=False, unique=True),
        ),
    ]
