"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tipo_treeking, Treeking
from .serializers import UserSerializer, LoginSerializer, Tipo_treekingSerializer, TreekingSerializer

@api_view(['GET','POST'])
def UserCrud(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_303_SEE_OTHER)
    elif request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET','POST'])
def LoginSet(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():            
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_303_SEE_OTHER)
#class UserViewSet(APIView):
    #def post(self,request):
    #    serializer = UserSerializer(data = request.data)
    #    if serializer.is_valid():
    #        user = serializer.save()
    #        return Response(serializer.data, status = status.HTTP_201_CREATED)
    #    else:
    #        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#class LoginViewSet(APIView):
    #def post(self,request):
    #    serializer = LoginSerializer(data = request.data)
    #    if serializer.is_valid():            
    #        return Response(serializer.data, status = status.HTTP_201_CREATED)
    #    else:
    #        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#class Tipo_treekingViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = Tipo_treeking.objects.all().order_by('Id_tipo')
#    serializer_class = Tipo_treekingSerializer    

#class TreekingViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = Treeking.objects.all().order_by('Id_tipo')
#    serializer_class = TreekingSerializer    