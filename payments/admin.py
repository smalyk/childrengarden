from django.contrib import admin
from .models import  Payment_made, Payment_needed, Child

class ChildAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'parent_phone', 'parent_email', 'discount']
    list_filter = ['discount']
    list_editable = ['parent', 'parent_phone', 'parent_email', 'discount']

#    class Meta:
#        verbose_name = u"Ребенок"
#        verbose_name_plural = u"Дети"

class Payment_madeAdmin(admin.ModelAdmin):
    list_display = ['name', 'contribution', 'payment_date']
    list_filter = ['name','payment_date']
    list_editable = ['contribution']

class Payment_neededAdmin(admin.ModelAdmin):
    list_display = ['category', 'address', 'reckoning', 'deadline', 'discount']
    list_filter = ['address','deadline', 'discount']
    list_editable = ['address', 'reckoning', 'deadline', 'discount']


admin.site.register(Payment_made, Payment_madeAdmin)
admin.site.register(Payment_needed, Payment_neededAdmin)
admin.site.register(Child, ChildAdmin)