from django.contrib import admin
from .models import *

# Display list of tables here
class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','mobile','email','message')

class categoryAdmin(admin.ModelAdmin):
    list_display=('id','CName','CPic','CDate')

class newsAdmin(admin.ModelAdmin):
    list_display=('id','ncity','nhead','ncategory','nsubject','ndes','ndate','npic')

class videonewsAdmin(admin.ModelAdmin):
    list_display=('id','vlink','vtitle','vnews','vcategory','vcity','vdate')

class notificationAdmin(admin.ModelAdmin):
    list_display=('id','ndes','ndate')

class sliderAdmin(admin.ModelAdmin):
    list_display=('id','spic','stitle','sdes','sdate')

# Register your models here.
admin.site.register(contact,contactAdmin)
admin.site.register(category,categoryAdmin)
admin.site.register(news,newsAdmin)
admin.site.register(videonews,videonewsAdmin)
admin.site.register(notification,notificationAdmin)
admin.site.register(slider,sliderAdmin)