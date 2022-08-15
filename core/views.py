from urllib.request import Request
from django.shortcuts import render, redirect
from .models import Person

def home(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {"persons": persons})

def save(request):
    namePerson = request.POST.get("name")
    Person.objects.create(name=namePerson)
    persons = Person.objects.all()
    return render(request, 'index.html', {"persons": persons})

def edit(request, id):
    person = Person.objects.get(id = id)
    return render(request, 'update.html', {"person": person})

def update(request, id):
    namePerson = request.POST.get("name")
    person = Person.objects.get(id=id)
    person.name = namePerson
    person.save()
    return redirect(home)

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(home)