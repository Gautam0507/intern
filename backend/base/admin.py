from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Meter

# Register your models here.


class MeterHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["__all__"]
    history_list_display = ["Last_recorded_reading", "Last_billed_reading"]


admin.site.register(Meter, SimpleHistoryAdmin)
