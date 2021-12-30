from django.db import models

# Create your models here.
from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model



# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name="UUID")
    class Meta:
        abstract = True

#class Profile(BaseModel):
#    user = models.OneToOneField(get_user_model(), related_name="profile", null=True, on_delete=models.SET_NULL, verbose_name="ユーザー")

class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name="タグ")
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="カテゴリ―")
    def __str__(self):
        return self.name

class Shop(BaseModel):
    shop_name = models.CharField(max_length=30,verbose_name="店の名前")
    catchphrase = models.TextField(verbose_name="キャッチフレーズ")
    postalcode = models.CharField(max_length=30,verbose_name="郵便番号",null=True,blank=True)
    address = models.CharField(max_length=250,verbose_name="住所",null=True,blank=True)
    address_image = models.ImageField(upload_to ="media/address",verbose_name="店の地図")
    url = models.URLField(max_length=250,verbose_name="ホームページURL",null=True,blank=True)
    instagram = models.URLField(max_length=250,verbose_name="インスタグラムURL",null=True,blank=True)
    twitter = models.URLField(max_length=250,verbose_name="ツイッターURL",null=True,blank=True)
    shop_detail = models.TextField(verbose_name="店の詳細")
    opening = models.CharField(max_length=250,verbose_name="営業時間",null=True,blank=True)
    contact = models.CharField(max_length=250,verbose_name="連絡先",null=True,blank=True)
    closed = models.CharField(max_length=250,verbose_name="定休日",null=True,blank=True)
    image = models.ImageField(upload_to ="media/image",verbose_name="店の画像")
    in_area_num = models.IntegerField(verbose_name="エリア内番号")
    item_name = models.CharField(max_length=30,verbose_name="物の名前")
    item_detail = models.TextField(verbose_name="物の詳細")
    stamp_image = models.ImageField(upload_to ="media/stamp",verbose_name="スタンプ")
    keyword = models.CharField(max_length=30,verbose_name="キーワード")
    origin = models.TextField(verbose_name="由来")


    category =models.ForeignKey(Category,verbose_name="カテゴリ―",on_delete=models.CASCADE,related_name="shops")
    tags = models.ManyToManyField(Tag,verbose_name="タグ",related_name="shops")

    stamp = models.ManyToManyField(get_user_model(),verbose_name="スタンプ",related_name="shops",through='Stamp')

    def __str__(self):
        return self.shop_name


class Stamp(BaseModel):
    shop = models.ForeignKey(Shop,verbose_name="店",related_name="stamps",on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),verbose_name="ユーザー",related_name="stamps",on_delete=models.CASCADE)
    judgement = models.BooleanField(default=False,blank=True,verbose_name="判定")

    
