from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('url', 'id', 'owner', 'task_name', 'deadline', 'completion')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
                many=True,
                view_name='todo-detail',
                read_only=True,
            )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'password', 'todos')
        extra_kwargs = {'password': {'write_only': True }}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user