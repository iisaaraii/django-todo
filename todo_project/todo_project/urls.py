from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # admin page
    path('', include('todo.urls')),   # include app-level urls
]
