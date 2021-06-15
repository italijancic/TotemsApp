# from django.db import models
from djongo import models
from django.utils import timezone

# Create your models here.

class Totem(models.Model):
	created_on = models.DateTimeField(default=timezone.now)
	device_id = models.CharField(max_length=17, blank=False, unique=True, null=True)
	label = models.CharField(max_length=100, blank=False, unique=True)
	location = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f"{self.device_id} : {self.label} - {self.location}"
