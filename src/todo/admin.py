from django.contrib import admin
# Register your models here.

from todo.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('task',)}