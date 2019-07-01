"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from .views import home,about,contectUs,login,blog,signup
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from myapp import form, views


urlpatterns = [

    path('', home,name='home' ),
    path('about/',about,name='about'),
    path('contect/',contectUs,name='contect'),
    # path('login/',login,name='login'),
    path('blog/',blog,name='blog'),
    # path('signup/',signup,name='signup'),
    #  path('login/',views.login,name='login'),
    # path('logout/',views.logout,name = 'logout'),
    #  path('login/',
    #      LoginView.as_view
    #      (
    #          template_name='login.html',
    #          authentication_form=form.userForm,
    #          extra_context=
    #          {
    #              'title': 'Log in',
                
    #          }
    #      ),
    #      name='login'),
    path('login/',login,name='login')
    
]