from django.db import models

class markaz(models.Model):
    markaz_USER = (
        ("Ingliz tili", "Ingliz tili"),
        ("koreys tili", "koreys tili"),
        ("rus tili", "rust tili"),
        ("arab tili", "arab tili"),
        ("mental arifmetika", "mental arifmetika"),
        ("matematika", "matematika"),
    )
    course = models.CharField(max_length=225, choices=markaz_USER)
    price = models.CharField(max_length=225, verbose_name="narxi", null=True)
    oyi = models.CharField(max_length=225, verbose_name="Kurs davomiyligi", null=True)


    def __str__(self):
        return self.course

