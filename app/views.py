from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view
from .forms import StudentForm, AppointmentForm
from app.models import Student,Appointment


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def classes(request):
    return render(request, 'classes.html')
def facility(request):
    return render(request, 'facility.html')
def team(request):
    return render(request, 'team.html')
def call(request):
    return render(request, 'call_to_action.html')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html',{'appointments': appointments})

def editappointment(request, id):
    appointments = get_object_or_404(Appointment ,id=id)
    if request.method == "POST":
        form1 = AppointmentForm(request.POST,instance=appointments)
        if form1.is_valid():
           form1.save()
           return redirect('appointment_list')
    else:
           form1 = AppointmentForm( instance=appointments)
    return render(request, 'editappointment.html',{'form1': form1, 'appointments': appointments})
def appointment_delete(request, id):
    appointments = get_object_or_404(Appointment ,id=id)
    try:
        appointments.delete()
    except Exception as e:
        messages.error(request,'Appointment not deleted')
    return redirect('appointment_list')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def editstudent(request, id):
    student = get_object_or_404(Student ,id=id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
           form.save()
           return redirect('student_list')
    else:
           form = StudentForm( instance=student)
    return render(request, 'editstudent.html',{'form': form, 'student': student})
def student_delete(request, id):
    student = get_object_or_404(Student ,id=id)
    try:
        student.delete()
    except Exception as e:
        messages.error(request,'Student not deleted')
    return redirect('student_list')

@api_view(['GET','POST'])
def appointmentapi(request):
    if request.method == "GET":
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def studentapi(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)

def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0799723671'
    amount = 1
    account_reference = 'emobilis'
    transaction_desc = 'Full Stack fee payment'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)