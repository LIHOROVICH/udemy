from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	#text = request['usertext']
	return render(request, 'example.html', {'name': 'Oleh'})
