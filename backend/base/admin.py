from .models import Meter
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from simple_history.admin import SimpleHistoryAdmin
from .models import Meter, Userinfo

# Register your models here.


class UserinfoInline(admin.StackedInline):
    model = Userinfo
    can_delete = False
    verbose_name_plural = 'userinfo'


class UserAdmin(BaseUserAdmin):
    inlines = (UserinfoInline,)


class MeterHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'Serial_number', 'user',
                    "Last_recorded_reading", "Last_billed_reading"]
    history_list_display = ["Last_recorded_reading", "Last_billed_reading"]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Meter)


admin.site.register(Meter, MeterHistoryAdmin)
