from django.shortcuts import render
from account.models import CustomUser
from django.db.models import Q

def Rating(request):
    users_list = CustomUser.objects.all()
    searched_users=[]
    if request.method == 'POST':
        searchUsertext = request.POST.get('searchUser')
        if searchUsertext:
            users = CustomUser.objects.filter(Q(first_name__icontains=searchUsertext) | Q(last_name__icontains=searchUsertext))
        else:
            users = users_list
        context={
            'users_list': users,
            'searchUsertext': searchUsertext
        }
        return render(request, 'rating/rating.html', context)
    context={
        'users_list': users_list
    }
    return render(request, 'rating/rating.html', context)

