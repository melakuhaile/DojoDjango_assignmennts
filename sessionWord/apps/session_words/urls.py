from django.conf.urls import url
from . import views
print "poop2"
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^clear$', views.clear)
    # url(r'^result$', views.result)
]