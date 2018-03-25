from django.conf.urls import url
from . import views
# import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='post_home'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/remove$', views.post_remove, name='post_remove'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^postlist_json/$', views.PostListJson.as_view(), name="post_list_json"),
]