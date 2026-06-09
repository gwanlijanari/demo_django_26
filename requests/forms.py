from django import forms    
from . models import Tutorial, Review

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['course', 'start_date', 'end_date', 'payment_method']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value']
