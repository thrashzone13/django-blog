from django.shortcuts import render, redirect
from django.contrib import messages
from pprint import pprint
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        pprint(dir(request.POST))
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Congratulations! Now you can log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'user/register.html', {
        'form': form,
        'title': "Sign up"
    })


@login_required
def profile(request):
    return render(request, 'user/profile.html')
