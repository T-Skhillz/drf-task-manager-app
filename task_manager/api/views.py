from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer

from ..models import Task

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user).order_by("-created_at")
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)