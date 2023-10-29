from django.contrib import admin
from .models import Cateogory, Course

# Register your models here.
@admin.register(Cateogory)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'short_desription', 'created_at')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'slug', 'short_desription','long_desription', 'created_at')