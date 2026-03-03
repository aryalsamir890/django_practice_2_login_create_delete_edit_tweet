from django.contrib import admin
from .models import tweet,products

class tweetAdmin(admin.ModelAdmin):
    list_display=('name','email','created_at','id')

class productAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_quantity')


admin.site.register(tweet,tweetAdmin)
admin.site.register(products,productAdmin)

