from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 1000}))
    rating = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])