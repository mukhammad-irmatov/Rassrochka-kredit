from django.contrib import admin
from .models import Kategoriya,Tovar,Xaridor,Tolov,Users_Message
# Register your models here.
class XaridorAdmin(admin.ModelAdmin):
    list_display = ['ism', 'familiya', 'pasportSeriyaRaqami','oylikTolovMiqdori','umumiyTolanganPul','qolganSumma']

class TovarAdmin(admin.ModelAdmin):
    list_display = ['nomi','narxi']

admin.site.register(Kategoriya)
admin.site.register(Tovar,TovarAdmin)
admin.site.register(Tolov)
admin.site.register(Xaridor,XaridorAdmin)
admin.site.register(Users_Message)

