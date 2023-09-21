from django.contrib import admin
from balapp.models import Balance
# Register your models here.
class BalanceAdmin(admin.ModelAdmin):
    list_display=['name','totalfees','paidfees','feebal']
admin.site.register(Balance,BalanceAdmin)
