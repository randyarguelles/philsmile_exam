from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^login/$',login ,name='login_time'),
    url(r'^logout/$',views.logout_page),
    #~ url(r'^emp/list/$', views.employee_list, name='employee_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^register/$',views.register_page),
    url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),
    url(r'^projects/$', views.project_list, name='project_list')

]