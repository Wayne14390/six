from django import forms

from app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'guardian_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your guardian name'}),
            'child_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your child name'}),
            'guardian_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your guardian email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your child age'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                       'accept': 'image/*',
                       'title': 'Select your image'
                       }
            ),
        }
