from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^payment$', views.payment),
    url(r'^checkout$', views.checkout),
    url(r'^clear$', views.clear)
]