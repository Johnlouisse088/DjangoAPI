from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('view_tasks/', views.view_tasks, name="view_tasks"),
    path('view_task/<int:id>/', views.view_task, name="view_task"),
    path('create_task/', views.create_task, name="create_task"),
    path('update_task/<int:id>/', views.update_task, name="update_task"),
    path('remove_task/<int:id>/', views.remove_task, name="remove_task"),
]

