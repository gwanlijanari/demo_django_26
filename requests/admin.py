from django.contrib import admin
from .models import Tutorial, Review
from unfold.admin import ModelAdmin

@admin.register(Tutorial)
class TutorialAdmin(ModelAdmin):
    list_filter = ["course"]
    list_display = ["title", "course", "student","status"]
    list_editable = ["status"]


@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ["student", "tutorial", "value"]