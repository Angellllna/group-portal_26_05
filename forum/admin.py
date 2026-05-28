from django.contrib import admin
from .models import ForumTopic, ForumComment

@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_closed')
    list_filter = ('is_closed', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)


@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
    ordering = ('created_at',)