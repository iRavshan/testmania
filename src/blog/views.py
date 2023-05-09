from django.shortcuts import render
from .models import Post

def Home(request):
    posts = Post.objects.all().order_by('created_at').values()
    context = {
        'posts': posts
    }
    return render(request, 'blog/explore.html', context)

def SingleBlog(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/single-blog.html', context)
