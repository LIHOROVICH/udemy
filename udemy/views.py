from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	#text = request['usertext']
	return render(request, 'example.html', {'name': 'Oleh'})


def reverse(request):
	text = request.GET['usertext']
	text = " ".join(text.split()[::-1])
	return render(request, 'reverse.html', {'usertext': text})
