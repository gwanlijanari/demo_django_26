from django.db import models
from courses.models import Course
from students.models import Student

class Tutorial(models.Model):
    class StatusChoice(models.TextChoices):
        new = "новая"
        active = "идет обучение"
        done = "обучение завершено"

    title = models.CharField("название", max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="tutorials", verbose_name="курс")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="tutorials", verbose_name="студент")
    status = models.CharField("статус", max_length=20, choices=StatusChoice.choices, default=StatusChoice.new)
    start_date = models.DateField("дата начала", null=True, blank=True)
    end_date = models.DateField("дата окончания", null=True, blank=True)
    payment_method = models.CharField("способ оплаты", max_length=50)

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"

    def __str__(self):
        return f"{self.student} - {self.course}"


class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="reviews", verbose_name="студент")
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="reviews", verbose_name="заявка")
    value = models.TextField("отзыв")

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
        unique_together = ("student", "tutorial")

    def __str__(self):
        return f"{self.student} - {self.tutorial}"