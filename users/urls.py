from django.urls import path
from .views import RegisterUserView, CustomTokenObtainPairView, UserSearchView, UserLogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('search/', UserSearchView.as_view(), name='search'),
]
