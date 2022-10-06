from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services" ),
    path('contacts/', views.contacts, name='contacts'),
    path('make_an_appointment/', views.make_an_appointment, name='appointment'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/',views.registerUser, name='register')
]