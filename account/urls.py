from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile-update/<int:pk>/', views.profileUpdate, name='profile-update'),
    path('profile-change-permission/<int:pk>/program/<int:pk2>', views.dummyView, name='profile-update'),
    path('profile-list/', views.profileList, name='profile-list'),
]
