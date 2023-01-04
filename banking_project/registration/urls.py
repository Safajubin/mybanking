from . import views
from django.urls import path
app_name='registration'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    path('form/', views.form, name='form'),
    path('logout', views.logout, name='logout'),


]
