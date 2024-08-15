from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField('name',max_length=100)
    name_en = models.CharField('name_en',max_length=100,)


    def __str__(self):
        return self.name



class User(AbstractUser):
    date_of_birth = models.DateField('Date of Birth', null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField('Статус администратора', default=False)
    REQUIRED_FIELDS = []

