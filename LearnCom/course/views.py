from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User

from .serializers import CourseListSerializer, CourseDetailSerializer, LessonSerializer, CommentSerializer, CategorySerializer, QuizSerializer, UserSerializer
from .models import Course, Lessons, Comment, Cateogory

# Create your views here.


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):

    categories = Cateogory.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_newest_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([])
# @permission_classes([])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonSerializer(course.lessons.all(), many=True)

    if request.user.is_authenticated:
        course_data = course_serializer.data
    else:
        course_data = {}

    return Response({
        'course': course_data,
        'lessons': lesson_serializer.data
    })


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    serizlizer = CommentSerializer(lesson.comments.all(), many=True)

    return Response(serizlizer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    course = Course.objects.get(slug=course_slug)
    lesson = Lessons.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course, lesson=lesson, name=data.get('name'), content=data.get('content'), created_by=request.user)

    serializer = CommentSerializer(comment)

    return Response(serializer.data)


@api_view(['GET'])
def get_quizes(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)

    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)

    return Response(serializer.data)


@api_view(['GET'])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = user.courses.all()

    user_serializer = UserSerializer(user, many=False)
    course_serializer = CourseDetailSerializer(courses, many=True)

    return Response({
        'courses': course_serializer.data,
        'created_by': user_serializer.data})
