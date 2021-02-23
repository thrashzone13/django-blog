from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'User: {username} created successfully')
            return redirect('login')
        else:
            messages.warning(request, list(form.error_messages.values())[0])
            return redirect('register')
    else:
        return render(request, 'user/register.html', {
            'form': UserCreationForm(),
            'title': "Sign up"
        })


def login(request):
    pass
