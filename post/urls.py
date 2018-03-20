from django.conf.urls import url
from . import views
# import views

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='post_home'),
    # url(r'^new/$', views.letter_new, name='letter_new'),
    # url(r'^(?P<pk>\d+)/edit$', views.letter_edit, name='letter_edit'),
    # url(r'^(?P<pk>\d+)/remove$', views.letter_remove, name='letter_remove'),
    # url(r'^(?P<pk>\d+)/$', views.letter_detail, name='letter_detail'),
    # url(r'^home/$', views.home, name='letter_home_json'),
    # url(r'^letter_list_json/$', views.LetterListJson.as_view(), name="letter_list_json"),
    
    # url(r'^list/$', views.student_list, name='student_list'),
    # url(r'^new/$', views.student_new, name='student_new'),
    # url(r'^list_json/$', login_required(views.student_list_json.as_view()), name="student_list_json"),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'student_list/$', views.StudentListJson.as_view(), name="student_list_json"),
    
]