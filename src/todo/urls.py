from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'todos', views.TodoViewSet, base_name='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]