from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from students.models import Student

class RegisterForm(UserCreationForm):
    name = forms.CharField(label="Имя", max_length=20)
    surname = forms.CharField(label="Фамилия", max_length=40)
    lastname = forms.CharField(label="Отчество", max_length=40, required=False)
    birth_date = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(label="Телефон", max_length=50)
    email = forms.EmailField(label="Почта", max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = user.student
            student.name = self.cleaned_data['name']
            student.surname = self.cleaned_data['surname']
            student.lastname = self.cleaned_data.get('lastname', '')
            student.birth_date = self.cleaned_data['birth_date']
            student.phone = self.cleaned_data['phone']
            student.email = self.cleaned_data['email']
            student.save()
        return user