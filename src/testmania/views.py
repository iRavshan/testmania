from django.shortcuts import render, redirect
from exam.models import Test, TestScore

def Home(request):
    tests = Test.objects.all().order_by('-created_at')[:3].values()
    context = {
        'tests': tests
    }
    return render(request, 'home.html', context)