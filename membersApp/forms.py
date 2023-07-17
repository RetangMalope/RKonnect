from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users import views

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Full Name',
            'email': 'Email Address',
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

class ProfileForm(ModelForm):
    class Meta:
        model = views.Profile
        fields = [
            'name', 'email', 'username', 'bio', 'short_intro', 'profile_image',
            'social_github', 'social_linkedin', 'social_twitter', 'social_youtube',
            'social_website'
        ]
