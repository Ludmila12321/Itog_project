from django.shortcuts import render

from administration_app.models import Animal

def animal_catalog(request):
    animals = Animal.objects.all()  # Получение всех объектов Animal

    return render(request, 'animal_catalog.html', {'animals': animals})