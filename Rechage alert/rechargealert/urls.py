"""
URL configuration for rechargealert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include
from app1 import views
# from . import views
# from . import views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.MainPage, name='main' ),

    path('airtelplan/' , views.AirtelPlanPage , name='airtelplan'),

    path('jioplan/' , views.jioplan , name='jioplan'),

    path('viplan/' , views.viplan , name='viplan'),

    path('netflixplan/' , views.netflixplan , name='netflixplan'),

    path('login/' , views.login , name='login'),

    path('signup/' , views.signup , name='signup'),

    path('disneyplan/' , views.disneyplan , name='disneyplan'),

    path('hotstarplan/' , views.hotstarplan , name='hotstarplan'),

    path('nomobilerecharge/' , views.nomobilerecharge, name='nomobilerecharge'),

    path('noottrecharge/' , views.noottrecharge, name='noottrecharge'),   

    path('countdown/', views.countdown, name='countdown'),

    path('', views.button_view, name='button_view'),

]
