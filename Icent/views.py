from django.shortcuts import render

# Create your views here.

def index(request):
	"""埃讯特的主页"""
	return render(request,'Icent/index.html')