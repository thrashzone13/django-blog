from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from pprint import pprint

# Create your views here.


def register(request):
    if request.method == 'POST':
        pprint(dir(request.POST))
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Now sign in')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {
        'form': form,
        'title': "Sign up"
    })


def login(request):
    pass
