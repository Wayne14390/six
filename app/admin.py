from django.contrib import admin

from app.models import Students
from app.views import studentrecords

# Register your models here.
admin.site.register(Students)