from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Event, Participant

# Customize User admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')

# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Event admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'eventDate', 'category', 'authorId', 'isDeleted', 'created_at')
    list_filter = ('eventDate', 'isDeleted', 'category')
    search_fields = ('name', 'description', 'category', 'authorId')
    date_hierarchy = 'eventDate'
    ordering = ('-eventDate',)

# Participant admin
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'get_event_name', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    
    def get_event_name(self, obj):
        return obj.eventId.name
    get_event_name.short_description = 'Event'
    get_event_name.admin_order_field = 'eventId__name'

# Register our models
admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
