"""
URL configuration for  project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('classes/', views.classes, name='classes'),
    path('facility/', views.facility, name='facility'),
    path('appointment/', views.appointment, name='appointment'),
    path('team/', views.team, name='team'),
    path('call_to_action/', views.call, name='call_to_action'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_delete/<int:id>/', views.student_delete, name='student_delete'),
    path('editstudent/<int:id>/', views.editstudent, name='editstudent'),
  ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
