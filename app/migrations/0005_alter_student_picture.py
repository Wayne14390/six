# Generated by Django 5.1.7 on 2025-03-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(upload_to='student_pictures/'),
        ),
    ]
