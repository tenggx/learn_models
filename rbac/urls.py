from django.conf.urls import url
from rbac import views


app_name = 'rbac'

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^base/', views.base),
    url(r'^test/', views.test),
]
