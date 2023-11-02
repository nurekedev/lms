from django.urls import path

from . import views

urlpatterns = [
    path('get_active_courses/', views.get_active_courses),
    path('track-started/<slug:course_slug>/<slug:lesson_slug>/', views.track_started),
    path('mark-as-done/<slug:course_slug>/<slug:lesson_slug>/', views.marks_as_done),

]