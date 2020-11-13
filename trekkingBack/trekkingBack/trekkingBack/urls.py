"""
Definition of urls for trekkingBack.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from app import forms, views

urlpatterns = [    
    path('', admin.site.urls),       
    path('create_user', views.UserCrud),
    path('Login_user', views.LoginSet),
    path('TipoTreeking_list', views.Tipo_TreekingSet),
    path('Treeking_list', views.TreekingSet)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
