from django.shortcuts import render
from .models import Episode
import random

# Create your views here.
def generator(request):
	context = {
		'episodes': Episode.objects.get(id=random.randint(1,188))
	}
	return render(request, 'offgen/generator.html', context)





