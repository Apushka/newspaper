from django.contrib import admin

from news.models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created',)

