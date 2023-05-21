from django.shortcuts import render
from account.models import CustomUser

def Rating(request):
    users_list = CustomUser.objects.all()
    context={
        'users_list': users_list
    }
    return render(request, 'rating/rating.html', context)

