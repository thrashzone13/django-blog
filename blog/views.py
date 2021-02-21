from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    print(request)
    return render(request, 'blog/home.html', {
        'title': "Home",
        'posts': Post.objects.all().order_by('-created_at'),
    })


def about(request):
    return render(request, 'blog/about.html')
