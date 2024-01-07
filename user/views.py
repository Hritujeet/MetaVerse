from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Logged in Successfully!')
            return redirect('feed')
        else:
            return HttpResponse('<h1>404 - User Not Found</h1><p>This account does not exist. Kindly check your '
                                'credentials or create an account.</p>')
    return render(request, 'user/login.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        phNo = request.POST.get('phNo')
        password = request.POST.get('pass')
        confpass = request.POST.get('confpass')

        if len(username) >= 3 and len(password) >= 8 and password == confpass:
            newUser = User.objects.create_user(username=username, password=password)
            newUser.first_name = fullname
            newUser.phoneNumber = phNo
            newUser.save()

            messages.add_message(request, messages.SUCCESS, 'Your account has been created! Login to continue.')
            return redirect('login')

    return render(request, 'user/signup.html')


def handleLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logged out Successfully!')
    return redirect("login")
