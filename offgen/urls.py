from django.urls import path
from . import views

urlpatterns = [
	path('', views.generator, name='generator'),
	path('display.html/', views.display, name='display'), # called when generator is clicked
]

