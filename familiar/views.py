from django.shortcuts import render

from .models import Familiar

def list_familiar(request):
    familiars = Familiar.objects.all()
    context = {'familiars': familiars}
    return render(request, 'index.html', context)
