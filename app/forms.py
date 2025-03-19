from django import forms

from app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['picture', 'student_name', 'student_bio']
        widgets = {
            'picture': forms.ClearableFileInput(
                        attrs={'class': 'form-control',
                       'accept':'image/*',
                       'title':'Select your image'
                       }
),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
