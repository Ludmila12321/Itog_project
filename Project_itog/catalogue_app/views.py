from django.shortcuts import render
from administration_app.models import Animal, Category, Gender

def animal_catalog(request):
    categories = Category.objects.all()
    genders = Gender.objects.all()

    selected_category = request.GET.get('category')
    selected_gender = request.GET.get('gender')

    animals = Animal.objects.all()

    if selected_category:
        animals = animals.filter(category__title=selected_category)

    if selected_gender:
        animals = animals.filter(gender__gender=selected_gender)

    return render(request, 'animal_catalog.html', {'animals': animals, 'categories': categories, 'genders': genders, 'selected_category': selected_category, 'selected_gender': selected_gender})