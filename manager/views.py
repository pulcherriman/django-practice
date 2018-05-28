from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *


class TaskListView(TemplateView):
    template_name = "task_list.html"

    def get(self, request, *args, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks
        return render(self.request, self.template_name, context)