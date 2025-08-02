from django.contrib import admin
from .models import Progress, Notification

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'completed', 'last_updated')
    list_filter = ('user', 'subject')
    search_fields = ('user__username', 'subject', 'notes')
    readonly_fields = ('last_updated',)
    fieldsets = (
        (None, {
            'fields': ('user', 'subject')
        }),
        ('Progress Details', {
            'fields': ('completed', 'notes', 'deadline')
        }),
        ('Dates', {
            'fields': ('last_updated',)
        }),
    )

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'notification_type', 'created_at', 'is_read')
    list_filter = ('notification_type', 'is_read')
    search_fields = ('title', 'message', 'user__username')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)
    date_hierarchy = 'created_at'