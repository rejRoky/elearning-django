from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=RegisterSerializer,
        responses={201: UserSerializer()},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Retrieve list of users",
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY, description="Search for users by username",
                type=openapi.TYPE_STRING
            )
        ],
        responses={200: UserSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        return CustomUser.objects.filter(
            username__icontains=search_term
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserLogoutView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Logout a user",
        responses={200: 'OK'}
    )
    def post(self, request):
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
