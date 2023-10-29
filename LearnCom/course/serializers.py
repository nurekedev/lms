from rest_framework import serializers
from .models import Cateogory, Course

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title','slug','short_desription')
