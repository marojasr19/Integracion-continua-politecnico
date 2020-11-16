"""
Definition of views.
"""

from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

def NewLogin(request):
    """Renders the about page."""
    if request.method == 'POST':
        accion = request.POST["accion"] 
        _UserName = request.POST["username"]
        _Password = request.POST["password"]
        _email = request.POST["email"]        

        if accion == "1":
            user = User.objects.create_user(username=_UserName,email=_email,password=_Password)
            login(request,user)

        elif accion == "0":
            Usuario = authenticate(username = _UserName, password=_Password)        

            if Usuario is not None:
                login(request,Usuario)    
            else:
                user = User.objects.create_user(username=_UserName,email=_email,password=_Password)
                login(request,user)

        return render(request,
            'app/index.html',
            {
                'title':'Login',                
                'year':datetime.now().year,                            
            })

    else:
        assert isinstance(request, HttpRequest)
        return render(request,
            'app/NewLogin.html',
            {
                'title':'Login',
                'message':'Your application description page.',
                'year':datetime.now().year,
            })

