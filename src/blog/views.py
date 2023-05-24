from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q

def Home(request):
    posts = Post.objects.all().order_by('-created_at').values()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def SingleBlog(request, id):
    post = get_object_or_404(Post, id=id)
    tags = post.tags.all()
    similar_posts = Post.objects.filter(tags__name__icontains=tags[0].name)[:3]
    last_news = Post.objects.all().order_by('-created_at').values()[:4]
    context = {
        'post': post,
        'related_to_topic': similar_posts,
        'last_posts': last_news
    }
    return render(request, 'blog/single-blog.html', context)
