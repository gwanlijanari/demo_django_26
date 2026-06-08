from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Transport, Course
from staff.models import Teacher

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ["transport","teacher"]
    list_filter = ["transport", "teacher"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            teacher = Teacher.objects.get(account=request.user)
            return qs.filter(teacher=teacher)
        except Teacher.DoesNotExist:
            return qs.none()
        

@admin.register(Transport)
class TransportAdmin(ModelAdmin):
    list_display = ["name"]