from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CourseListSerializer, CourseDetailSerializer, LessonSerializer, CommentSerializer
from .models import Course, Lessons, Comment

# Create your views here.


@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_newest_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }

    return Response(data)


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    serizlizer = CommentSerializer(Comment.objects.all(), many=True)

    return Response(serizlizer.data)



@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    course = Course.objects.get(slug=course_slug)
    lesson = Lessons.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course, lesson=lesson, name=name, content=content, created_by=request.user)
    
    serializer = CommentSerializer(comment)

    return Response(serializer.data)
