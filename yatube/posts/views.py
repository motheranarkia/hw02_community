from django.shortcuts import get_object_or_404, render
from .models import Post, Group

POSTS_COUNT = 10
# Create your views here.

def index(request):
    title = 'Yatube_project'
    posts = Post.objects.order_by('-pub_date')[:POSTS_COUNT]
    context = {
        'title':title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    title = 'Записи сообщества'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POSTS_COUNT]
    context = {
        'group':group,
        'posts':posts,
    }
    return render(request, 'posts/group_list.html', context)
