from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

def loginUser(request):

    page = 'login'
    if  request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  # Fixed variable name

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
            return redirect('login')  # Redirect back to login page

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'membersApp/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'You are logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Additional processing or saving logic can be added here
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            # Redirect to the desired page after successful registration
            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.success(request, 'An error occurred. Please try again')

    context = {'page': page, 'form': form}
    return render(request, 'membersApp/login_register.html', context)