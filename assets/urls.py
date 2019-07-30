from django.conf.urls import url
from . import views

app_name = 'assets'

urlpatterns = [
    url('report/', views.report, name='report'),
    url('^dashboard/$', views.dashboard, name='dashboard'),
    url('^index/$', views.index, name='index'),
    url('^detail/<int:asset_id>/$', views.detail, name="detail"),
    url('^$', views.dashboard),
]