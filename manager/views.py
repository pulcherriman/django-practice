from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from .forms import TaskForm
from manager.models import *


class TaskListView(TemplateView):
    template_name = "task_list.html"
    def get(self, request, *args, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks
        return render(self.request, self.template_name, context)

#class TaskAddView(TemplateView):
def add(request):
	if request.method == 'POST':
		task = Task()
		taskform = TaskForm(request.POST, instance=task)
		if taskform.is_valid():
			task = taskform.save(commit=False)
			task.save()
	else:
		taskform = TaskForm()
	context = {
		'form': taskform,
	}
	return render(request, 'task_add.html', context)
