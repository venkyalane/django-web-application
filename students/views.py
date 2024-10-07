from django.shortcuts import render
from students.models import Student
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def get_data(request):
    data = Student.objects.all()
    paginator = Paginator(data, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "employee.html", context={'data':page_obj, 'page':'Students'})