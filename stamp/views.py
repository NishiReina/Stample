# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Stamp,Shop
import random



def index(request):
    return render(request, 'stamp/index.html')

@login_required
def original(request):
    request.session['count']=2
    if request.method == 'POST':
        
        return render(request,'stamp/original.html')

def original_route(request):
    
    user_data = request.user
    if request.method == 'POST':
        checkbox_list = request.POST.getlist("tag_and_category")
        score_list = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0]]

        for i in range(len(checkbox_list)):
            for j in range(1,16):
                shop = Shop.objects.get(in_area_num=j)
                tags =  shop.tags.all()

                if shop.category.name == checkbox_list[i]:
                    score_list[j-1][1] += 1

                for k in range(len(tags)):
                    if tags[k].name==checkbox_list[i]:
                        score_list[j-1][1] += 1


        score_list=sorted(score_list,key=lambda x: x[1], reverse=True)
        original_list = [score_list[0][0],score_list[1][0],score_list[2][0],score_list[3][0],score_list[4][0]]
        original_list = sorted(original_list)
       
        request.session['key']=original_list
        stamps=[]
        for i in range(len(original_list)):
            shop = Shop.objects.get(in_area_num = original_list[i])
            stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
            stamps.append(stamp)
        return render(request,'stamp/mount.html',{'stamps':stamps})


def random_route(request):
    request.session['count']=2
    user_data = request.user
    if request.method == 'POST':
        random_list = random.sample(range(1,16), 5)
        random_list=sorted(random_list)

        request.session['key']=random_list
        stamps=[]
        for i in range(len(random_list)):
            shop = Shop.objects.get(in_area_num = random_list[i])
            stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
            stamps.append(stamp)
    return render(request,'stamp/mount.html',{'stamps':stamps})

def check_stamp_number(request):
    count = 0
    user_data = request.user
    first_register=request.session['count']
    for i in range(1,16):
        shop = Shop.objects.get(in_area_num=i)
        stamp = Stamp.objects.get(user=user_data.uuid,shop=shop.uuid)
        if stamp.judgement:
            count += 1
    if count == 5:
        request.session['count']=first_register+1
    updated_first_register=request.session['count']
    if updated_first_register==1:
        return True
    return False
        
def home(request):
    stamp_list = request.session['key']
    user_data = request.user
    stamps = []
    register_check=check_stamp_number(request)
    for i in range(len(stamp_list)):
        shop = Shop.objects.get(in_area_num = stamp_list[i])
        stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
        stamps.append(stamp)
    if register_check:
        context={'stamps':stamps,'register_message1':"ユーザー登録しませんか？",'register_message2':"次回に続きから再開できるようになります。",'register_message3':"右下のログインボタンから登録できます。"}
    else:
        context={'stamps':stamps,'register_message':None}
    return render(request,'stamp/home.html',context)

def route(request):
    stamp_list = request.session['key']
    user_data = request.user
    stamps = []

    for i in range(len(stamp_list)):
        shop = Shop.objects.get(in_area_num = stamp_list[i])
        stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
        stamps.append(stamp)
           
    return render(request,'stamp/route.html',{'stamps':stamps})


def user_picturebook(request):
    user_data = request.user
    stamps = Stamp.objects.filter(user=user_data.uuid)
    count = 0
    for i in range(0,15):
        if (stamps[i].judgement) == True:
            count += 1
    collection_rate = (count/15)*100
    collection_rate = int(collection_rate)
    context = {'stamps':stamps,
                   'collection_rate':collection_rate}#stampのテーブル特定
    return render(request,'stamp/picturebook.html',context)


def check_shop(input_shop_name):
    shops = []
    for i in range(1,16):
        shop = Shop.objects.get(in_area_num=i)
        shops.append(shop.shop_name)
    if input_shop_name not in shops:
        return False
    return True 


    

def stamp_to_home(request):
    user_data = request.user
    if request.method == 'POST':
        input_shop_name =request.POST.get('shop_name')
        input_keyword = request.POST.get('keyword')
        shop_check=check_shop(input_shop_name)
        if shop_check :
            shop = Shop.objects.get(shop_name=input_shop_name)
            stamp = Stamp.objects.get(user=user_data.uuid,shop=shop.uuid)
            if shop.keyword==input_keyword:
                stamp.judgement = True
                stamp.save()
                context = {"stamp":stamp}
                return render(request,'stamp/stamp_get.html',context)
            elif shop.keyword!=input_keyword:
                stamp_list=request.session['key']
                stamps = []

                for i in range(len(stamp_list)):
                    shop = Shop.objects.get(in_area_num = stamp_list[i])
                    stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
                    stamps.append(stamp)
                    context={'stamps':stamps,
                    'message':"キーワードが間違っています"}
                return render(request,'stamp/home.html',context)
        else :
            stamp_list=request.session['key']
            stamps = []
            for i in range(len(stamp_list)):
                shop = Shop.objects.get(in_area_num = stamp_list[i])
                stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
                stamps.append(stamp)
            context={'stamps':stamps,
                    'message':"店の名前が間違っています"}
            return render(request,'stamp/home.html',context)


def stamp_to_route(request):
    user_data = request.user
    if request.method == 'POST':
        input_shop_name =request.POST.get('shop_name')
        input_keyword = request.POST.get('keyword')
        shop_check=check_shop(input_shop_name)
        if shop_check :
            shop = Shop.objects.get(shop_name=input_shop_name)
            stamp = Stamp.objects.get(user=user_data.uuid,shop=shop.uuid)
            if shop.keyword==input_keyword:
                stamp.judgement = True
                stamp.save()
                context = {"stamp":stamp}
                return render(request,'stamp/stamp_get.html',context)
            elif shop.keyword!=input_keyword:
                stamp_list=request.session['key']
                stamps = []

                for i in range(len(stamp_list)):
                    shop = Shop.objects.get(in_area_num = stamp_list[i])
                    stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
                    stamps.append(stamp)
                    context={'stamps':stamps,
                    'message':"キーワードが間違っています"}
                return render(request,'stamp/route.html',context)
        else :
            stamp_list=request.session['key']
            stamps = []
            for i in range(len(stamp_list)):
                shop = Shop.objects.get(in_area_num = stamp_list[i])
                stamp = Stamp.objects.get(user = user_data.uuid,shop=shop.uuid)
                stamps.append(stamp)
            context={'stamps':stamps,
                    'message':"店の名前が間違っています"}
            return render(request,'stamp/route.html',context)


def stamp_to_picturebook(request):
    user_data = request.user
    if request.method == 'POST':
        
        input_shop_name =request.POST.get('shop_name')
        input_keyword = request.POST.get('keyword')

        shop_check=check_shop(input_shop_name)
        if shop_check :
            shop = Shop.objects.get(shop_name=input_shop_name)
            stamp = Stamp.objects.get(user=user_data.uuid,shop=shop.uuid)
            if shop.keyword==input_keyword:
                stamp.judgement = True
                stamp.save()
                context = {"stamp":stamp}
                return render(request,'stamp/stamp_get.html',context)
            elif shop.keyword!=input_keyword:
                stamps = Stamp.objects.filter(user=user_data.uuid)
                count=0
                for i in range(0,15):
                    if (stamps[i].judgement)==True:
                        count+=1
                collection_rate=(count/15)*100
                collection_rate=int(collection_rate)
                context = {'stamps':stamps,
                            'collection_rate':collection_rate,
                            'message':"キーワードが間違っています",
                            }
                return render(request,'stamp/picturebook.html',context)
        else :
            stamps = Stamp.objects.filter(user=user_data.uuid)
            count=0
            for i in range(0,15):
                if (stamps[i].judgement)==True:
                    count+=1
            collection_rate=(count/15)*100
            collection_rate=int(collection_rate)
            context = {'stamps':stamps,
                        'collection_rate':collection_rate,
                        'message':"店の名前が間違っています",}
            return render(request,'stamp/picturebook.html',context)


def detail(request,shop_uuid):
    shop = Shop.objects.get(pk=shop_uuid)
    shop_data = {'shop':shop}
    return render(request,'stamp/detail.html',shop_data)

def to_change_page(request):
    return render(request,'stamp/change.html')








