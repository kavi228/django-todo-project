from django import forms
from todolist.models import ToDoItem

class ToDoItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["title", "description"]
        labels = {
            "title": ("Название"),
            "description": ("Описание")
        }

class ToDoItemUpdateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["title", "description", "done"]
        labels = {
            "title": ("Название"),
            "description": ("Описание"),
            "done": ("Выполнено"),
        }

