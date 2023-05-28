from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import CustomUser
from .validators import CheckConfirmationPassword, CleanUsername

def Register(request):
    context={}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context['form'] = form
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if(not CleanUsername(username)):
            context['username_error'] = 'Ushbu foydalanuvchi nomi allaqachon band'
            return render(request, 'account/register.html', context)
        if(not CheckConfirmationPassword(password, confirm_password)):
            context['confirm_password_error'] = 'Tasdiqlash paroli mos kelmadi'
            return render(request, 'account/register.html', context)

        if form.is_valid():
            form.save()
            new_user = authenticate(request, username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('home')  
    else:
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

@login_required(login_url="/account/login")
def Logout(request):
    logout(request)
    return render(request, 'account/login.html')

@login_required(login_url="/account/login")
def Settings(request):
    if request.method == 'GET':
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

def Delete(request, username):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(username=username)
            user.delete()
        except:
            messages.error(request, 'The user not found')
        return redirect('/')