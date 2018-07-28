from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import viewsets, permissions, mixins
from todo.models import Todo
from todo.serializers import TodoSerializer, UserSerializer
from todo.permissions import IsOwnerOrAdminUser, IsSelfOrAdminUser

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (
        IsOwnerOrAdminUser,
    )
    lookup_field = 'slug'

    def perform_create(self, serializer):
        slug_target_value = serializer.validated_data['task']
        slug = slugify(slug_target_value, allow_unicode=True)
        serializer.save(owner=self.request.user, slug=slug)

    def perform_update(self, serializer):
        slug_target_value = serializer.validated_data['task']
        slug = slugify(slug_target_value, allow_unicode=True)
        serializer.save(slug=slug)

    def get_queryset(self):
        # get object that object owner is authenticated (logged in) user
        current_user = self.request.user
        if current_user.is_staff:
            return Todo.objects.all()

        return Todo.objects.filter(owner=current_user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (
        IsSelfOrAdminUser,
    )
    lookup_field = 'username'

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_staff:
            return User.objects.all()

        return User.objects.filter(username=current_user.username)