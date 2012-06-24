from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^date/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'uploadpictures.views.urldate', name='date'),
      url(r'^viewpictures/$', 'uploadpictures.views.viewpicture'),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^viewpictures/$', direct_to_template, {'template': 'viewpictures.html'}), 

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)



if settings.DEBUG:
	urlpatterns+= patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
		}),
	)
