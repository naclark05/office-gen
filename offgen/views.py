from django.shortcuts import render

# Create your views here.
def generator(request):
	return render(request, 'offgen/generator.html')