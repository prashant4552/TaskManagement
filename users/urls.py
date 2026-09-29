from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-task/', views.create_task, name='create_task'),
    path('edit-task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete_task'),
]