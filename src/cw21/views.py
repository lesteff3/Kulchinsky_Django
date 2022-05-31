from django.shortcuts import render
from django.http import HttpResponseRedirect
from cw21.models import Student


def home_page(request):
    if request.method == 'GET':
        student = Student.objects.all()
        context = {
            'student': student
        }
        return render(request, 'home.html', context=context)
    return HttpResponseRedirect('/')


def create(request):
    if request.method == 'POST':
        people = Student()
        people.first_name = request.POST.get('first_name')
        people.last_name = request.POST.get('last_name')
        people.age = request.POST.get('age')
        people.profession = request.POST.get('profession')
        people.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/cw21/create/')
    return render(request, 'add_person.html')
