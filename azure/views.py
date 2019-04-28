from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def novel_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'azure/novel_list.html', {'posts': posts})

def curate_novel_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'azure/novel_list.html', {'posts': posts, 'curate': 'valid'})

def novel_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'azure/novel_detail.html', {'post': post})

def curate_novel_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'azure/novel_detail.html', {'post': post, 'curate': 'valid'})

