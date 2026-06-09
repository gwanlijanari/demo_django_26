from django import forms    
from . models import Tutorial, Review

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ["title", "course", "start_date", "payment_method"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value']
