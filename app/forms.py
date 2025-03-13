from django import forms

from app.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-control','placeholder': 'Enter your gender'}),
            'date_of_birth':forms.DateInput(attrs={'class': 'form-control','placeholder': 'Enter your D.O.B'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                       'accept':'image/*',
                       'title': 'Select an image'}
            )
        }