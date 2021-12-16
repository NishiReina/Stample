# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Stamp,Shop
# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'stamp/index.html')

@login_required
def original(request):
    if request.method == 'POST':
        return render(request,'stamp/original.html')

def random(request):
    if request.method == 'POST':
        return render(request,'stamp/mount.html')

           


