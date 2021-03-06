from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/data$', views.post_data, name='post_data'),
    url(r'^post/zyczenia$', views.zyczenia, name='zyczenia'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
