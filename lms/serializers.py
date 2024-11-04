from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = serializers.SerializerMethodField()

    def get_lessons_qty(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ['pk', 'name', 'preview', 'description', 'lessons_qty', ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
