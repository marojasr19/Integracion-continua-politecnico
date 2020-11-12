"""
Definition of urls for trekkingBack.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from app import forms, views

#router = routers.DefaultRouter()
#router.register(r'TipoTreek', views.Tipo_treekingViewSet)
#router.register(r'Treek', views.Tipo_treekingViewSet)

urlpatterns = [    
    path('', admin.site.urls),
    #path('api', include(router.urls)),
    #path('create_user/', views.UserViewSet.as_view(),name='api_create_user'),
    #path('login_user/', views.LoginViewSet.as_view(),name='api_login_user'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))    
    path('create_user', views.UserCrud),
    path('Login_user', views.LoginSet),
]

urlpatterns = format_suffix_patterns(urlpatterns)
