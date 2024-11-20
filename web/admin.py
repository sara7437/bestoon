from django.contrib import admin
from .models import Expense,Income

# ثبت مدل Expense در پنل مدیریت
admin.site.register(Expense)
admin.site.register(Income)
