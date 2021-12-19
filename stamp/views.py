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
        
        return render(request,'stamp/original.html')

def original_route(request):
    if request.method == 'POST':
        checkbox_list=request.POST.getlist("tag_and_category")

        for i in range(len(checkbox_list)):
            for j in range(1,3):#for j in range(1,16):
                count=1
        return render(request,'stamp/mount.html')

def random_route(request):
    if request.method == 'POST':
        random_list = random.sample(range(1,3), 2)#random_list = random.sample(range(1,16), 5)
        return render(request,'stamp/mount.html')

def user_picturebook(request):
    if request.method == 'POST':
        user_data = request.user
        stamps = Stamp.objects.filter(user=user_data.uuid
        )


        count=0
        for i in range(0,2):
            if (stamps[i].judgement)==True:
                count+=1
            collection_rate=(count/2)*100
            collection_rate=int(collection_rate)

        context = {'stamps':stamps,
                   'collection_rate':collection_rate}#stampのテーブル特定
        
        
    return render(request,'stamp/picturebook.html',context)

           


