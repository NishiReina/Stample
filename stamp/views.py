# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Stamp,Shop
import random
# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'stamp/index.html')

@login_required
def original(request):
    if request.method == 'POST':
        #checkbox_list = request.POST.getlist["tag_and_category"]
        return render(request,'stamp/original.html')

def original_route(request):
    if request.method == 'POST':
        #checkbox_list = request.POST.getlist["tag_and_category"]
        return render(request,'stamp/mount.html')

def random_route(request):
    if request.method == 'POST':
        random_list = random.sample(range(1,3), 2)#random_list = random.sample(range(1,16), 5)
        return render(request,'stamp/mount.html')

           


