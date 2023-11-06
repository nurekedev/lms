from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
from django.utils.text import slugify
import random

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
    courses = Course.objects.filter(status=Course.PUBLISHED)

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_newest_courses(request):
    courses = Course.objects.filter(status=Course.PUBLISHED)[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([])
# @permission_classes([])
def get_course(request, slug):
    course = Course.objects.filter(status=Course.PUBLISHED).get(slug=slug)
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


@api_view(['POST'])
def create_course(request):
    print(request.data)

    status = request.data.get('status')

    if status == 'published':
        status = 'draft'

    course = Course.objects.create(
        title=request.data.get('title'),
        slug='%s-%s' % (slugify(request.data.get('title')), random.randint(1000,10000)),
        short_desription=request.data.get('short_desription'),
        long_desription=request.data.get('long_desription'),
        status=status,  
        created_by=request.user
        )
    
    for id in request.data.get('categories'):
        course.categories.add(id)

    course.save()

    for lesson in request.data.get('lessons'):
        tmp_lesson = Lessons.objects.create(
            course=course,
            title=lesson.get('title'),
            slug=slugify(lesson.get('title')),
            short_desription=lesson.get('short_desription'),
            long_desription=lesson.get('long_desription'),
            status=Lessons.DRAFT,


        )

    
    print("")
    return Response({'course_id':course.id})


@api_view(['GET'])
def get_quizes(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)

    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)

    return Response(serializer.data)


@api_view(['GET'])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = user.courses.filter(status=Course.PUBLISHED)

    user_serializer = UserSerializer(user, many=False)
    course_serializer = CourseDetailSerializer(courses, many=True)

    return Response({
        'courses': course_serializer.data,
        'created_by': user_serializer.data})
