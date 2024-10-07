from django.shortcuts import render, redirect
from peaple.models import People
from django.contrib.auth.decorators import login_required



# Create your views here.
def home_people(request):
    return render(request, "vote_home.html", context = {'page':'Peoples'})

@login_required(login_url = '/login/')
def add_people_form(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        address = data.get('address')
        People.objects.create(
            name = name,
            age = age,
            address = address
            )
        return redirect('https://venkyalane.pythonanywhere.com/all-people/')
    return render(request, "add_people.html", context = {'page':'Add People Form'})

@login_required(login_url = '/login/')
def delete_people(request, id):
    data = People.objects.get(id = id)
    data.delete()
    return redirect('https://venkyalane.pythonanywhere.com/')

@login_required(login_url = '/login/')
def all_people(request):
    data = People.objects.all()
    return render(request, "all_peoples.html", context= {'peoples':data, 'page':'All Peoples'})


