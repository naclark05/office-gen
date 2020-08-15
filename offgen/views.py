from django.shortcuts import render
from .models import Episode
from django.template import loader
import random

# Create your views here.

def generator(request): # base view

	return render(request, 'offgen/generator.html')

def display(request): # call this view when clicking generator button
	try:
		context = {
	 	'episodes': Episode.objects.get(id=random.randint(3,190))
		}
	except Episode.DoesNotExist:
		pass
	return render(request, 'offgen/display.html', context)










