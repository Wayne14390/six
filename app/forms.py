from django import forms

from app.models import Student,Appointment


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

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['guardian_name', 'guardian_email', 'child_name','child_age','message']
        widgets = {
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_email': forms.TextInput(attrs={'class': 'form-control'}),
            'child_name': forms.TextInput(attrs={'class': 'form-control'}),
            'child_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }