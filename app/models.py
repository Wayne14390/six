from django.db import models

# Create your models here
class Students(models.Model):
    image = models.ImageField(upload_to='nurses_images/',blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name