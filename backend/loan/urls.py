
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    
    url(r'api/list', views.get_users_list, name='get_users_list')
    
]