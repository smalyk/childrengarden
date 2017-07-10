from django.contrib import admin
from .models import  Payment_made, Payment_needed, Child





admin.site.register(Payment_made)
admin.site.register(Payment_needed)
admin.site.register(Child)