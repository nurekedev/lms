from django.urls import path
from course import views


urlpatterns = [
    path('', views.get_courses),
    path('get-newest-courses/', views.get_newest_courses),
    path('get-categories/', views.get_categories),
    path('create/', views.create_course),
    path('<slug:slug>/', views.get_course),
    path('get-author-course/<int:user_id>/', views.get_author_courses),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/', views.get_comments),
    path('<slug:course_slug>/<slug:lesson_slug>/get-quiz/', views.get_quizes),

] 
