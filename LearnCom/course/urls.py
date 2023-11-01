from django.urls import path
from course import views


urlpatterns = [
    path('', views.get_courses),
    path('get-newset-courses/', views.get_newest_courses),
    path('get-categories/', views.get_categories),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments', views.get_comments),
] 
