from django.shortcuts import render,redirect
from django.contrib.auth import login
import string, random
from accounts.models import User#勝手に初めて、勝手にログインする機能
from stamp.models import Stamp,Shop

def signup_original(request):
    if request.method == 'POST':
        user_data = User.objects.create(
            username = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])),
            email = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)]))+"example.com",
            password = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])),
        )
        #中間テーブルに登録したい
        for i in range(1,3):#for i in range(1,16):
            Stamp.objects.create(
                shop = Shop.objects.get(in_area_num=i),
                user = user_data,
            )
        
        
        login(request, user_data)
        
    return render(request,'stamp/original.html')

def signup_random(request):
    if request.method == 'POST':
        user_data = User.objects.create(
            username = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])),
            email = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)]))+"@example.com",
            password = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])),
        )
        #中間テーブルに登録したい
        for i in range(1,3):#for i in range(1,16):
            Stamp.objects.create(
                shop = Shop.objects.get(in_area_num=i),
                user = user_data,
            )
        
        login(request, user_data)
        stamps = []
        random_list = random.sample(range(1,3), 2)#random_list = random.sample(range(1,16), 5)
        random_list = sorted(random_list)
        request.session['key']=random_list
        for i in range(1,len(random_list)+1):
            shop = Shop.objects.get(in_area_num = i)
            stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
            stamps.append(stamp)
        
        
    return render(request,'stamp/mount.html',{'stamps':stamps})

#アカウント引継ぎのための、メールアドレスとパスワード変更
def change(request):
    user_data = request.user
    if request.method == 'POST':
        user_data.email = request.POST.get('email')
        user_data.password =request.POST.get('password')
        user_data.save()
        return render(request,'stamp/index.html')