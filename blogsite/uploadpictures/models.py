from django.db import models
import os
from django.conf import settings

#class Filefield(upload_to = os.path.join(PROJECT_ROOT,'media')[, max_length=1000, **options])

class Picture(models.Model, ):
	caption = models.CharField(blank=True, max_length= 50)
	image = models.ImageField(upload_to='uploads/')
	pub_date = models.DateTimeField('Date uploaded')
	
# Create your models here.
