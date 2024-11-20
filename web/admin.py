from django.contrib import admin
from .models import Expense

# ثبت مدل Expense در پنل مدیریت
admin.site.register(Expense)
