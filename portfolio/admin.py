from django.contrib import admin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'codename', 'specialization', 'level')
    list_filter = ('specialization', 'level')
    search_fields = ('user__username', 'codename', 'skills')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Основне', {
            'fields': ('user', 'codename', 'specialization', 'level', 'avatar')
        }),
        ('Профіль', {
            'fields': ('bio', 'skills', 'achievements')
        }),
        ('Службове', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
