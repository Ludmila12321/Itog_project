from django.shortcuts import render
from administration_app.models import New

def index(request):
    news_list = New.objects.all().order_by('-date_added')  # список новостей, сортированный по дате добавления
    return render(request, 'index.html', {'news_list': news_list})

def about(request):
    return render(request, 'about.html')