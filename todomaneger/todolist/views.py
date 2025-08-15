from django.shortcuts import render
from .models import ToDoItem

def vid_view(request):
    todoitems = ToDoItem.objects.order_by("id").all()
    return render(request, "todolist/vid.html", context={"todoitems": todoitems})