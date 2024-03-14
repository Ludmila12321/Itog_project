from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, ReviewForm
from .models import Review

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Ссылаемся на главную страницу

@login_required
def reviews_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = Review(user=request.user, text=form.cleaned_data['text'], rating=form.cleaned_data['rating'])
            new_review.save()
            return redirect('reviews_page')

    form = ReviewForm()
    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'reviews_page.html', {'form': form, 'reviews': reviews})