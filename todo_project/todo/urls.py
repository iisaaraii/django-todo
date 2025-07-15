from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
]
