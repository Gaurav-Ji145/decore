from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list = ("name", "mobile_no", "eamil", "message")


admin.site.register(User, UserAdmin)


