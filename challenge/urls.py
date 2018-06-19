from django.conf.urls import url
from django.contrib import admin

from database import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name='welcome'),
    url(r'^list$', views.list, name='list'),
    url(r'^add$', views.add, name='add'),
]
