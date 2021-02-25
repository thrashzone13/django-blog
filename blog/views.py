from typing import Optional
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'blog/home.html', {
        'title': "Home",
        'posts': Post.objects.all().order_by('-created_at'),
    })


class PostListView(ListView):
    model = Post
    # template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self) -> Optional[bool]:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self) -> Optional[bool]:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {
        'title': "About"
    })
