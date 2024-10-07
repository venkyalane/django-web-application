"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from peaple import views as peopleviews
from vege import views as vegeviews
from students import views as studentsviews
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('age-calculate/', views.age_calculate, name='age_calculate'),
    path('javascript-practice/', views.javascript, name='javascript'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_page, name='logout_page'),

    path('student/', studentsviews.get_data, name='get_data'),

    path('people-home/', peopleviews.home_people, name='home_people'),
    path('add-people-form/', peopleviews.add_people_form, name='add_people_form'),
    path('delete/<id>/', peopleviews.delete_people, name='delete_people'),
    path('all-people/', peopleviews.all_people, name='all_people'),

    path('recipies_home/', vegeviews.home_recipies, name='home_recipies'),
    path('add-recipies/', vegeviews.add_recipies, name='add_recipies'),
    path('show-recipies/', vegeviews.show_recipies, name='show_recipies'),
    path('delete/<id>/', vegeviews.delete_recipies, name='delete_recipies'),
    path('update/<id>/', vegeviews.update_recipies, name='update_recipies'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()