from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'course']
        widgets = {
                'phone_number': forms.TextInput(attrs={
                'pattern': r'^\+?1?\d{9,15}$',
                'title': 'Phone number format: +9999999999 (up to 15 digits)'
            }),
        }