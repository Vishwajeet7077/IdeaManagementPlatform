from django.urls import path, include
from . import views

urlpatterns = [
    path('idea/<int:pk>/', views.ideaView, name='idea'),
    path('idea-list/', views.ideaList, name='idea-list'),
    path('program/<int:pk>/idea-create/', views.ideaCreate, name='idea-create'),
    path('idea-update/<int:pk>/', views.dummyView, name='idea-update'),
    path('idea-delete/<int:pk>/', views.dummyView, name='idea-delete'),
    path('idea-change-status/<int:pk>/', views.dummyView, name='idea-change-status'),
    path('unauthorized-access', views.dummyView, name='unauthorized-access'),
]
