from django.shortcuts import render

from .models import Post
from django.views.generic import ListView, DetailView, CreateView


# class 기반
class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'head_image']



# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/post_list.html', {'posts': posts, })
#
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post, })
