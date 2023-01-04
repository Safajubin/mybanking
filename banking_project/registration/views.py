from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/registration/form')
        else:
            messages.info(request, "invalid details")
            return redirect('/registration/login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('/registration/login')
        else:
            messages.info(request, "password not matching")
            return redirect('/registration/register')
        return redirect('/')
    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    return render(request, 'form.html')
