from django.contrib import admin
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_message', 'gemini_response', 'timestamp']
    search_fields = ['user__username', 'user_message', 'gemini_response']
    list_filter = ['timestamp']

admin.site.register(ChatMessage, ChatMessageAdmin)
