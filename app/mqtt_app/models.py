from djongo import models
from django.utils import timezone

# Create your models here.

class Msg(models.Model):
	device_id = models.CharField(max_length=17, blank=False, unique=True, null=True)
	user_dni = models.IntegerField(unique=True, blank=False)
	user_temp = models.IntegerField(blank=False)

	class Meta:
		abstract = True


class TotemMsg(models.Model):
	_id = models.ObjectIdField()
	created_on = models.DateTimeField(default=timezone.now)
	msg = models.EmbeddedField(
        model_container = Msg
    )
