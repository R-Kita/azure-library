from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

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

def curate_novel_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form  = PostForm(instance=post)
    return render(request, 'azure/novel_edit.html', {'form': form, 'curate': 'valid'})
