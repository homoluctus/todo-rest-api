from django.contrib.auth.models import User
from rest_framework import serializers, fields
from todo.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('url', 'owner', 'slug', 'task', 'deadline', 'completion')
        read_only_fields = ('slug',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='todo-detail',
        read_only=True,
        lookup_field='slug',
    )

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'todos')
        extra_kwargs = {
            'url': {'lookup_field': 'username'},
            'password': {'write_only': True },
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance