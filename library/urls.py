from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),

    path('add/',
         views.add_book,
         name='add_book'),

    path('register/', views.register, name='register'),
    
    path('theme/', views.set_theme, name='set_theme'),

    path('login/', views.student_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),


]