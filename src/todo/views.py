from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from todo.models import Todo
from todo.serializers import TodoSerializer, UserSerializer
from todo.permissions import IsOwnerOrAdminUser, IsCurrentUserOrAdminUser

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (
        IsOwnerOrAdminUser,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_staff:
            return Todo.objects.all()

        return Todo.objects.filter(owner=current_user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (
        IsCurrentUserOrAdminUser,
    )

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_staff:
            return User.objects.all()

        return User.objects.filter(username=current_user.username)