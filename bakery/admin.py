from django.contrib import admin
from .models import *

class OrderProductInline(admin.TabularInline):
    model = OrderProduct

class OrderAdmin(admin.ModelAdmin):
    inlines=[(OrderProductInline)]

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)






