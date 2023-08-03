from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import (Category, CategorySerializer,
                          Post, PostSerializer,
                          Comment, CommentSerializer,
                          Like, LikeSerializer)

class FixView(ModelViewSet):
    pass

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff