from django.contrib import admin

from hoarding.models import Item, CollectionSchedule


class ItemAdmin(admin.ModelAdmin):
    pass


class CollectionScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(CollectionSchedule, CollectionScheduleAdmin)
