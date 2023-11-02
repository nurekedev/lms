from django.contrib import admin
from .models import Activity

# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'course', 'status', 'created_by', 'created_at',)