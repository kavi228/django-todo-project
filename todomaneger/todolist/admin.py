from django.contrib import admin

from todolist.models import ToDoItem

@admin.register(ToDoItem)
class ToDoItem(admin.ModelAdmin):
    list_display = "id", "title", "done", "description"
