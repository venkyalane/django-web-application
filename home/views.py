from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from log import LogClass


log = LogClass().get_the_logs()
# Create your views here.
def home(request):
    return render(request, "home.html", context = {'page':'Home'})

def about(request):
    return render(request, "about.html", context = {'page':'About'})

def contact(request):
    return render(request, "contact.html", context = {'page':'ContactUs'})

def age_calculate(request):
    return render(request, "age_calculate.html", context = {'page':'Age Calculator'})

def javascript(request):
    return render(request, "javascript.html", context = {'page':'JavaScript Practice'})

def register_page(request):
    if request.method == "POST":
        log.info("Register Method Called")
        log.info("First name entered")
        first_name = request.POST.get('first_name')
        log.info("Last name entered")
        last_name = request.POST.get('last_name')
        log.info("Username entered")
        username = request.POST.get('username')
        log.info("Password entered")
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already taken!!!')
            log.info("Username already taken!!!")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username)

        user.set_password(password)
        user.save()
        log.info(f"{username} Account created successfully...")
        messages.info(request, 'Account created successfully...')
        return redirect('/login/')
    return render(request, "register.html", context={'page':'Register'})


def login_page(request):
    if request.method == "POST":
        log.info("Login method called")
        username = request.POST.get('username')
        log.info("Username entered")
        password = request.POST.get('password')
        log.info("Password entered")

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username!!!')
            log.info("Invalid username entered")
            return redirect('/login/')

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'Invalid Passwod!!!!')
            log.info("Invalid password entered")
            return redirect('/login/')

        else:
            login(request, user)
            log.info(f"{username} Login successfully...")
            return redirect('https://venkyalane.pythonanywhere.com/')
    return render(request, "login.html", context={'page':'Login'})



def logout_page(request):
    logout(request)
    log.info("logout successfully...")
    return redirect('/login/')