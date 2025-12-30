from django.contrib import admin
from .models import tweet

class tweetAdmin(admin.ModelAdmin):
    list_display=('name','email','created_at','id')


admin.site.register(tweet,tweetAdmin)

