from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from students.models import Student

@receiver(post_save, sender=User)
def create_student_for_user(sender, instance, created, **kwargs):
    if created and not instance.is_staff and not instance.is_superuser:
        Student.objects.create(account=instance, name='', surname='')