from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^toupiao/(\d+)/$',views.toupiao,name='toupiao')
]