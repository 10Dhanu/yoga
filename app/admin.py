from django.contrib import admin
from .models import YogaClass, Booking

@admin.register(YogaClass)
class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'schedule')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'service', 'location', 'instructor', 'date', 'time', 'booking_date')
    search_fields = ('user_name', 'user_email', 'service', 'instructor')
    list_filter = ('service', 'location', 'instructor', 'date')
