from .models import Meter
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Userinfo
# Register your models here.


class UserinfoInline(admin.StackedInline):
    model = Userinfo
    can_delete = False
    verbose_name_plural = 'userinfo'


class UserAdmin(BaseUserAdmin):
    inlines = (UserinfoInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Meter)
