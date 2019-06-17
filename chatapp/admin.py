from django.contrib import admin

# Register your models here.
from chatapp.models import TextMessage

class TextMessageAdmin(admin.ModelAdmin):
    list_display = ['__str__','sent_at']

admin.site.register(TextMessage, TextMessageAdmin)