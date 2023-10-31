from rest_framework import serializers
from .models import Cateogory, Course, Lessons


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_desription')


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_desription', 'long_desription',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id', 'title', 'slug', 'short_desription', 'long_desription',)
