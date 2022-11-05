from typing import Hashable
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Hashtag
from .forms import PostForm, CommentForm, HashtagForm
from django.utils import timezone

# Create your views here.
def main(request):
    return render(request, 'main.html')

def create(request, post = None):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('read')
        else :
            form = PostForm(instance=post)
            return render(request, 'create.html', {'form':form})
        
    else:
        form = PostForm
        return render(request, 'create.html', {'form':form})
    
def read(request):
    posts = Post.objects
    return render(request, 'read.html', {'posts':posts})

def detail(request, id):
    posts = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.postid = posts
            comment.text = form.cleaned_data['text']
            comment.save()
            id = id
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'posts':posts, 'form':form})

def edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('detail', post.id)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})
    
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('read')

def update_comment(request, id, com_id):
    post = get_object_or_404(Post, id=id)
    comment = get_object_or_404(Comment, id=com_id)
    form = CommentForm(instance=comment)
    if request.method=="POST":
        update_form = CommentForm(request.POST, instance = comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail', id)
    return render(request, 'update_comment.html', {'form':form, 'post':post, 'comment':comment})

def hashtag(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = '이미 존재하는 해시태그입니다.'
                return render(request, 'hashtag.html', {'form':form, 'error_message':error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'hashtag.html', {'form':form})
def likes(request, id):
    like = get_object_or_404(Post, id = id)
    if request.user in like.post_like.all():
        like.post_like.remove(request.user)
        like.like_count -= 1
        like.save()
    
    else:
        like.post_like.add(request.user)
        like.like_count += 1
        like.save()
        
    return redirect('detail', like.id)