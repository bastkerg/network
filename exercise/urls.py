from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^restart$', views.restart, name='restart'),
        url(r'^next$', views.next, name='next'),
	url(r'^validate$', views.validate, name='validate'),
]
