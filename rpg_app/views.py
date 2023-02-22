from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.http import HttpResponse
import os
# class IndexView()


def index(request):
    port = os.environ.get('PORT', 8000)
    return render(request, 'rpg_app/index.html', {'port': port})


def form_submit(request):
    if request.method == 'POST':
        my_input = request.POST['my_input']
        # Do something with the input data
        submitted = True
        return render(request, 'form.html', {'submitted': submitted})
    else:
        return render(request, 'form.html')
