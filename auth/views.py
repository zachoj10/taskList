from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext


def login_page(request):
    return render_to_response('auth/auth.html', context_instance=RequestContext(request))

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            username = user.username
            return HttpResponseRedirect('/user/%d'%request.user.id)
        else:
            return render_to_response('auth/auth_failed.html', context_instance=RequestContext(request))
    else:
        return render_to_response('auth/invalid_login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')