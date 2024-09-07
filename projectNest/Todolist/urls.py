from django.urls import path

from . import views


app_name = 'Todolist'


urlpatterns = [
    path('add/', views.add, name='add'),
]