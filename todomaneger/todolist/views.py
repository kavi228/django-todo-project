from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import ToDoItem
from .forms import ToDoItemCreateForm, ToDoItemUpdateForm
from django.urls import reverse, reverse_lazy


def vid_view(request):
    todoitems = ToDoItem.objects.order_by("id").all()
    return render(request, "todolist/vid.html", context={"todoitems": todoitems})

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm

    def get_success_url(self):
        return reverse("todolist:vid")

class ToDoDetailView(DetailView):
    model = ToDoItem

class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = '_update_form'
    form_class = ToDoItemUpdateForm

    def get_success_url(self):
        return reverse("todolist:vid")

class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todolist:vid")