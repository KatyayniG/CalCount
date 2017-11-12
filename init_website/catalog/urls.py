from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_cal_count', views.get_cal_count, name='get_cal_count')
]

