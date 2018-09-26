from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('rooms/', views.getrooms, name='index'),
	path('gettoken/', views.gettoken, name='gettoken'),
]