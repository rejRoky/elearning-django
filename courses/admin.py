from django.contrib import admin
from .models import Course, Enrollment, CourseMaterial, Feedback


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher', 'created_at')
    search_fields = ('title', 'teacher__username')
    list_filter = ('created_at',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')


@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'file', 'uploaded_at')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
