from django.contrib import admin

from .models import Tiyatro


@admin.register(Tiyatro)
class TiyatroAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'video_url']
    list_display = ('id', 'title', 'content', 'video_url', 'status', 'created_at', 'updated_at')
