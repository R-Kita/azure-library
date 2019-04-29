from django.shortcuts import redirect, render, get_object_or_404
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
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('curate_novel_detail', pk=post.pk)
    else:
        form  = PostForm(instance=post)
        return render(request, 'azure/novel_edit.html', {'form': form, 'curate': 'valid'})

def curate_novel_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('curate_novel_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'azure/novel_edit.html', {'form': form, 'curate': 'valid'})


