import datetime
import time
from datetime import date
from django.http import HttpResponse
from django import forms
from django.template import Context, loader
from uploadpictures.models import Picture
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def urldate(request, year, month, day):
	published_date = datetime.date(int(year), int(month), int(day))
	return HttpResponse(published_date.ctime())

def viewpicture(request):
	picture = Picture.objects.all()	
	t = loader.get_template('uploadpictures/viewpictures.html')
	c = Context({
        'pictures': picture,
   	 })
	#return HttpResponse(t)
	#render_to_response('uploadpictures/viewpictures.html', {'picture': picture})
	return HttpResponse(t.render(c))

 
