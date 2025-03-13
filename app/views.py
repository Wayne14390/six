from django.shortcuts import render, redirect

from app.forms import StudentsForm


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
def appointment(request):
    return render(request, 'appointment.html')
def team(request):
    return render(request, 'team.html')
def call(request):
    return render(request, 'call-to-action.html')
def studentrecords(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentrecords')
    else:
        form = StudentsForm()
    return render(request, 'studentrecords.html',{'form':form})
