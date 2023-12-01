from django.db import models


class Teacher(models.Model):
    TEACHER_USER = (
        ("Ingliz tili", "Ingliz tili"),
        ("Rus tili", "Rus tili"),
        ("Arab tili", "Arab tili"),
        ("Koreys tili", "Koreys tili"),
    )
    surname = models.CharField(max_length=225, verbose_name="Ism Familiya")
    course = models.CharField(max_length=255, choices=TEACHER_USER, )
    phone = models.CharField(max_length=225, verbose_name="Telefon raqami")
    experience = models.CharField(max_length=225, verbose_name="tajribasi")
    img = models.ImageField(verbose_name="O'qituvchining rasmi", upload_to="teacher_img")

    about = models.TextField

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
