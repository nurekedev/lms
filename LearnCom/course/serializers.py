from rest_framework import serializers
from .models import Cateogory, Course, Lessons, Comment, Quiz



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cateogory
        fields = ('id', 'title', 'slug')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_desription', 'get_image',)


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug',
                  'short_desription', 'long_desription',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id', 'title', 'slug', 'lesson_type',
                  'short_desription', 'long_desription',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at',)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson_id', 'question', 'answer', 'option1', 'option2', 'option3')
