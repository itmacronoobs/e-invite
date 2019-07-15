from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name= 'index'),
	url(r'^excel$', views.excel, name= 'excel')
]