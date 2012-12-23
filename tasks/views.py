from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from tasks.models import Task, User
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request, user_id):
	username = get_object_or_404(User, pk=user_id)
	task_list = Task.objects.all().order_by('date_due')
	return render_to_response('tasks/index.html', {'task_list': task_list, 'username': username, 'user_id':user_id})

def detail(request, user_id, task_id):
	task = Task.objects.get(pk=task_id)
	return render_to_response('tasks/detail.html', {'task': task})
