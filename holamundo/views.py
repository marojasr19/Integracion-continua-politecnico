from django.http import HttpResponse
from django.template import loader

def inicio(request):
    template = loader.get_template('holamundo/inicio.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))