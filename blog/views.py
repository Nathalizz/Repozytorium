

from .models import Post

from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'klucz': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_data(request):
    return render(request, 'blog/post_data.html')

def zyczenia(request):
    return render(request, 'blog/zyczenia.html')
