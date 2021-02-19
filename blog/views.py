from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Reza',
        'title': 'First post',
        'content': 'First post content',
        'date': '10-10-1999'
    },
    {
        'author': 'Reza',
        'title': 'Second post',
        'content': 'Second post content',
        'date': '10-10-1999'
    }
]


def home(request):
    return render(request, 'blog/home.html', {
        'title': "Home",
        'posts': posts,
    })


def about(request):
    return render(request, 'blog/about.html')
