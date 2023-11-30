from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="mylist"),
    path('updatetask/<str:pk>/', views.updateTask, name="updatetask"),
    path('deletetask/<str:pk>/', views.deleteTask, name="deletetask"),
]