from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Course, Feedback, CourseMaterial
from .serializers import CourseSerializer, FeedbackSerializer, CourseMaterialSerializer
from rest_framework.response import Response


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class CourseEnrollView(generics.UpdateAPIView):
    serializer_class = CourseSerializer

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'message': 'Enrolled successfully'})


class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class CourseMaterialCreateView(generics.CreateAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer
    permission_classes = [IsAuthenticated]
