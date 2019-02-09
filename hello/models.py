from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Latlong(models.Model):
	latitude = models.CharField(max_length=100)
	longitude = models.CharField(max_length=100)

	def __unicode__(self):
		return self.latitude + " " + self.longitude