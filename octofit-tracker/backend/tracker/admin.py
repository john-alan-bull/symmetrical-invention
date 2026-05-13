from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_minutes', 'created_at')
    ordering = ('-created_at',)
