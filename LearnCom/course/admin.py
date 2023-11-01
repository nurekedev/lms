from django.contrib import admin
from .models import Cateogory, Course, Lessons, Comment

# Register your models here.
class LessonCommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['lesson']

@admin.register(Cateogory)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'short_desription', 'created_at')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'short_desription',
                    'long_desription', 'created_at')


@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'short_desription',
                    'long_desription', 'course', 'lesson_type')
    list_filter = ['status', 'lesson_type']
    search_fields = ['title', 'short_desription', 'long_desription']
    inlines = [LessonCommentInline]
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content',)



