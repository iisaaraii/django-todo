from django.urls import path
from . import views
from .views import TaskListView 


urlpatterns = [
     # also import TaskDetailView when adding detail view

    path('', TaskListView.as_view(), name='index'),

   # path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('add/', views.add_task, name='add_task'),
]
