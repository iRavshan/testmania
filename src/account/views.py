from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import CustomUser

def Register(request):
    context={}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            checked_user = CustomUser.objects.filter(username=username).exists()
            if(checked_user):
                context['form'] = form
                context['error'] = 'Ushbu foydalanuvchi nomi band'
            new_user = authenticate(request, username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('home')
    form = SignUpForm()
    context['form'] = form
    return render(request, 'account/register.html', context)

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Foydalanuvchi nomi yoki parol xato')
        return redirect('login')
    return render(request, 'account/login.html')

@login_required(login_url="/account/login/")
def Logout(request):
    logout(request)
    return render(request, 'account/login.html')

@login_required(login_url="/account/login/")
def Settings(request):
    user = CustomUser.objects.get(id=request.user.id)
    context={
        'user': user
    }
    return render(request, 'account/settings.html', context)


def Profile(request, username):
    user = CustomUser.objects.get(username=username)
    context = {
        'user': user
    }
    return render(request, 'account/profile.html', context)