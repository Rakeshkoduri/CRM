from django.contrib import admin
from .models import *
# Register your models here.



class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    field = '__all__'



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
# admin.site.register(CustomerAdmin)

