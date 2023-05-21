from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def error_404(request, exception):
    return render(request, '404.html')