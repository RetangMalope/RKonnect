from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users import views
from .forms import ProfileForm, SkillForm

# Create your views here.

@login_required(login_url = 'login')
def membersAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile':profile, 'skills': skills, 'projects': projects}
    return render(request, 'membersProfiles/account.html', context)


@login_required(login_url = 'login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'membersProfiles/profile_form.html', context)