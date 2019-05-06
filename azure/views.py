from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .recomend.model_gen import model_gen
from .recomend.topic_gen import topic_gen

def novel_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    for post in posts:
        text = post.text[:1000].split()
        post.text = " ".join(text[:100]) + "..."
    return render(request, 'azure/novel_list.html', {'posts': posts})

def curate_novel_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    for post in posts:
        text = post.text[:1000].split()
        post.text = " ".join(text[:100]) + "..."
    return render(request, 'azure/novel_list.html', {'posts': posts, 'curate': 'valid'})

def novel_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    recs = Post.objects.all().filter(topic_id_1st=post.topic_id_1st).exclude(pk=post.pk)[:3]
    for rec in recs:
        text = rec.text[:1000].split()
        rec.text = " ".join(text[:100]) + "..."
    return render(request, 'azure/novel_detail.html', {'post': post, 'recs': recs})

def curate_novel_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    recs = Post.objects.all().filter(topic_id_1st=post.topic_id_1st).exclude(pk=post.pk)[:3]
    for rec in recs:
        text = rec.text[:1000].split()
        rec.text = " ".join(text[:100]) + "..."
    return render(request, 'azure/novel_detail.html', {'post': post, 'recs': recs, 'curate': 'valid'})

def curate_novel_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            topic_line_up = topic_gen([post.text])
            post.topic_id_1st = topic_line_up[0]
            post.topic_id_2nd = topic_line_up[1]
            post.topic_id_3rd = topic_line_up[2]
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
            topic_line_up = topic_gen([post.text])
            post.topic_id_1st = topic_line_up[0]
            post.topic_id_2nd = topic_line_up[1]
            post.topic_id_3rd = topic_line_up[2]
            post.save()
            return redirect('curate_novel_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'azure/novel_edit.html', {'form': form, 'curate': 'valid'})


