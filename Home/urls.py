from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='Home'),
    path ("about/",views.about, name='about'),
    path ("services/",views.services, name='services'),
    path ("contact/",views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]