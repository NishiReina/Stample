from django.contrib import admin

# Register your models here.
from . models import Tag
from . models import Category
from . models import Shop
from . models import Stamp
#from . models import Profile
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Stamp)
#admin.site.register(Profile)