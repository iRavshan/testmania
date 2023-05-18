from django.shortcuts import render
from .models import Post

def Home(request):
    posts = Post.objects.all().order_by('-created_at').values()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def SingleBlog(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/single-blog.html', context)
