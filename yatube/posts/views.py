from django.shortcuts import get_object_or_404, render

from .models import Post, Group

POST_COUNT = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:POST_COUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POST_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
