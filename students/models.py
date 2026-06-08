from django.db import models
from django.conf import settings

class Student(models.Model):
    name = models.CharField("имя", max_length=20)
    surname = models.CharField("фамилия", max_length=40)
    lastname = models.CharField("отчество", max_length=40, blank=True)
    birt_date = models.DateField("дата рождения")
    phone = models.CharField("номер телефона", max_length=50)
    email = models.EmailField("почта", max_length=50)
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student",
        verbose_name="аккаунт"
    )
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["surname", "name"]

    def __str__(self):
        return f"{self.surname} {self.name} {self.lastname}"


