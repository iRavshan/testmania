from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm(),
            context = {
                'form':form
            }
            
    return render(request, 'account/register.html', context)

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('salom')
        messages.error(request, 'Foydalanuvchi nomi yoki parol xato')
        return redirect('login')
    return render(request, 'account/login.html')

def Logout(request):
    logout(request)
    return render(request, 'account/login.html')
