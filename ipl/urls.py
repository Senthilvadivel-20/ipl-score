
from django.contrib import admin
from django.urls import path
from .import views

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('result/',views.result,name='result'),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
