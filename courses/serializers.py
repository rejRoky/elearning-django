from rest_framework import serializers
from users.models import CustomUser
from .models import Course
from .models import Feedback, CourseMaterial


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['student', 'course', 'rating', 'comment']


class CourseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = ['course', 'file']


# Serializer for enrolled students
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name']


# Serializer for courses
class CourseSerializer(serializers.ModelSerializer):
    # Use the Enrollment model to retrieve students for this course
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'students', 'created_at']
