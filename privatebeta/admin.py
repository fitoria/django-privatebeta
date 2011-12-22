from django.contrib import admin
from privatebeta.models import InviteRequest

def send_invite(modeladmin, request, queryset):
    for element in queryset:
        element.send_invite()
send_invite.short_description = "Send invite to user"

class InviteRequestAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('email', 'created', 'invited',
                    'invited_date', 'used_invitation')
    list_filter = ('created', 'invited',)
    actions = [send_invite]

admin.site.register(InviteRequest, InviteRequestAdmin)
