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
	latitude = latlong.latitude
	longitude = latlong.longitude

	response = HttpResponse()
	response.status_code = 200
	response.content = "The food cart is last spotted at https://www.google.com/maps/search/?api=1&query=%s,%s" % (latitude, longitude)
	response.write = "The food cart is last spotted at https://www.google.com/maps/search/?api=1&query=%s,%s" % (latitude, longitude)
	
	return render(request, "query.html", {"latitude": latitude, "longitude": longitude})

def submit(request, latitude = "0", longitude = "0"):
	latlong = Latlong()
	latlong.latitude = latitude
	latlong.longitude = longitude
	latlong.save()

	return render(request, "empty.html")
