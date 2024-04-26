from django.contrib import admin
from conversations.models import Conversation, Message
# Register your models here.


class ConversationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at", "count_messages")


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message)
