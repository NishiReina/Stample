from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
import string, random
from accounts.models import User#勝手に初めて、勝手にログインする機能
from stamp.models import Stamp,Shop

def signup_original(request):
    request.session['count']=0
    if request.method == 'POST':
        user_data = User.objects.create(
            username = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])),
            email = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)]))+"@example.com",
            password = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])),
        )
        #中間テーブルに登録したい
        for i in range(1,16):
            Stamp.objects.create(
                shop = Shop.objects.get(in_area_num=i),
                user = user_data,
            )
        
        
        login(request, user_data)
        
    return render(request,'stamp/original.html')

def signup_random(request):
    request.session['count']=0
    if request.method == 'POST':
        user_data = User.objects.create(
            username = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])),
            email = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)]))+"@example.com",
            password = (''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])),
        )
        #中間テーブルに登録したい
        for i in range(1,16):
            Stamp.objects.create(
                shop = Shop.objects.get(in_area_num=i),
                user = user_data,
            )
        
        login(request, user_data)
        stamps = []

        random_list = random.sample(range(1,16), 5)
        random_list=sorted(random_list)


        request.session['key']=random_list
        for i in range(len(random_list)):
            shop = Shop.objects.get(in_area_num = random_list[i])
            stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
            stamps.append(stamp)
        
        
    return render(request,'stamp/mount.html',{'stamps':stamps})

#アカウント引継ぎのための、メールアドレスとパスワード変更
def change(request):
    user_data = request.user
    if request.method == 'POST':
        if request.POST.get('password')==request.POST.get('password2'):
            user_data.email = request.POST.get('email')
            user_data.set_password(request.POST.get('password'))
            user_data.save()
            
            logout(request)
            return render(request,'stamp/index.html')
            
        elif request.POST.get('password')!=request.POST.get('password2'):
            context={'message':"パスワードをもう一度入力してください"}
            return render(request,'stamp/change.html',context)

        