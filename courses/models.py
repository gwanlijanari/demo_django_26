from django.db import models


class Transport(models.Model):
    name = models.CharField("название", max_length=50)
    created_at = models.DateTimeField("создано", auto_now_add=True)
    updated_at = models.DateTimeField("обновлено", auto_now=True)

    class Meta:
        verbose_name = "транспорт"
        verbose_name_plural = "транспорт"
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.name
    
class Course(models.Model):
    code = models.CharField("код", max_length=15)
    about = models.CharField("описание", max_length=200,blank=True)
    course_start = models.DateField("дата начала", null=True, blank=True)
    course_end = models.DateField("дата окончания", null=True, blank=True)
    transport = models.ForeignKey(
        Transport,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
        verbose_name="транспорт"
    )

    teacher = models.ForeignKey(
    'staff.Teacher',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="courses",
    verbose_name="преподаватель"
)

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["transport__name"]
        indexes = [
            models.Index(fields=["teacher"]),
            models.Index(fields=["transport"])
        ]

    def __str__(self):
        return f"{self.code} - {self.transport}" if self.transport else self.code
