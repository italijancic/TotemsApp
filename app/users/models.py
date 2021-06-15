# from django.db import models
from djongo import models
from django.utils import timezone
# from phone_field import PhoneField

# Create your models here.

class User(models.Model):
	created_on = models.DateTimeField(default=timezone.now)
	first_name = models.CharField(max_length=64, blank=False)
	last_name = models.CharField(max_length=64, blank=False)
	dni = models.IntegerField(unique=True, blank=False)
	# cel = PhoneField(blank=True, help_text='Contact phone number')
	email = models.EmailField(max_length=64, blank=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"