from django.contrib.auth.models import AbstractUser
from django.db import models
from teacher.models import Teacher

class User(models.Model):
    yoshi = models.CharField(max_length=225, verbose_name="O'qituvchining yoshi", null=True)
    surname = models.CharField(max_length=225, verbose_name="ism , familiya")
    teacher = models.CharField(max_length=225, verbose_name="O'qituvchi")
    number = models.CharField(max_length=225, verbose_name="Telefon nomer")
    message = models.TextField(default="Siz 4K english academyda ro'yxatdan o'tdingiz", blank=True, verbose_name="Boshqa ma'lumotlar")

    def __str__(self):
        return self.surname

