from django.shortcuts import render, redirect
from vege.models import recipi
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_recipies(request):
    return render(request, "recipies_home.html", context={'page':'Recipies'})

@login_required(login_url = '/login/')
def add_recipies(request):
    if request.method == "POST":
        recipi_name = request.POST.get('recipi_name')
        recipi_desc = request.POST.get('recipi_desc')
        recipi_img = request.FILES.get('recipi_img')
        recipi.objects.create(
            recipi_name = recipi_name,
            recipi_desc = recipi_desc,
            recipi_img = recipi_img)
        return redirect('https://venkyalane.pythonanywhere.com/show-recipies/')
    return render(request, "recipi.html", context={'page':'Add Recipies Form'})

def show_recipies(request):
    qryset = recipi.objects.all()
    if request.POST.get('search'):
        qryset.filter(recipi_name__icontains = request.get('search'))
    return render(request, "show_recipi.html", context = {'page':'All Recipies', 'data': qryset})

@login_required(login_url = '/login/')
def delete_recipies(request, id):
    qryset = recipi.objects.get(id=id)
    qryset.delete()
    return redirect('https://venkyalane.pythonanywhere.com/show-recipies/')

@login_required(login_url = '/login/')
def update_recipies(request,id):
    qryset = recipi.objects.get(id=id)
    if request.method == "POST":
        recipi_name = request.POST.get('recipi_name')
        recipi_desc = request.POST.get('recipi_desc')
        recipi_img = request.FILES.get('recipi_img')
        qryset.recipi_name =recipi_name
        qryset.recipi_desc =recipi_desc
        if recipi_img:
            qryset.recipi_img = recipi_img
        qryset.save()
        return redirect('https://venkyalane.pythonanywhere.com/show-recipies/')
    return render(request, "update_recipi.html", context={'page':'Update Recipies Form','data':qryset})


