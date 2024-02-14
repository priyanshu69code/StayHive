from django.contrib import admin
from conversations.models import Converstions, Message
# Register your models here.


class ConversationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at", "count_messages")


admin.site.register(Converstions, ConversationAdmin)
admin.site.register(Message)
