from django.urls import path, include
from users.views import RegisterUserAPIView
from news.views import NewModelViewSet, LikeOrUnlikeAPIView
from comments.views import CommentModelViewSet

from rest_framework.authtoken import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'news', NewModelViewSet)
router.register(r'comments', CommentModelViewSet)

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('likes/<int:pk>/', LikeOrUnlikeAPIView.as_view()),

]