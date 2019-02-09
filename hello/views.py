from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Latlong

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def query(request):
	latlong = Latlong.objects.order_by('-id')[0]
	latitude = latlong["latitude"]
	longitude = latlong["longitude"]
	return render(request, "query.html", {"latitude": latitude, "longitude": longitude})

def submit(request):
	latitude = request.GET("lat")
	longitude = request.GET("lon")
	latlong = Latlong()
	latlong.latitude = latitude
	latlong.longitude = longitude
	latlong.save()

	return
