from django.shortcuts import render,redirect
# from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, 'User/index.html')



def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'User/login.html')
    return render(request, 'User/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'Home/signup.html', {'message': 'username already exist'})
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('/')

    return render(request, 'User/signup.html')

def handleLogout(request):
    logout(request)
    return redirect('/')

@login_required
def quiz(request):
    return render(request, 'User/quiz.html')