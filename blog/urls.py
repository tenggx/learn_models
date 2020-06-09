from django.conf.urls import url, include
from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^hello_world/', views.hello_world),
    url(r'^content/', views.article_content),
    url(r'^index/', views.get_index_page, name="index"),
    # url(r'^$', views.get_index_page, name="index"),
    # url(r'^detail/<int:article_id>', views.get_detail_page),
    # url(r'^detail/<int:article_id>', views.get_detail_page),
    path('', views.get_index_page, name='home'),
    path('detail/<int:article_id>', views.get_detail_page),

]
