from django.db import models

class Student(models.Model):
    picture = models.ImageField(upload_to='student_pictures/')
    student_name = models.CharField(max_length=255)
    student_bio = models.TextField()

    def __str__(self):
        return self.student_name

class Appointment(models.Model):
    guardian_name = models.CharField(max_length=255)
    guardian_email = models.EmailField()
    child_name = models.CharField(max_length=255)
    child_age = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.guardian_name