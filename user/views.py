from django.shortcuts import render, redirect
from django.contrib import messages
from pprint import pprint
from .forms import UserRegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        pprint(dir(request.POST))
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Now sign in')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'user/register.html', {
        'form': form,
        'title': "Sign up"
    })


def login(request):
    return render(request, 'user/login.html', {
        'title': 'Sign in'
    })
