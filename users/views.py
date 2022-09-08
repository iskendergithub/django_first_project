from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as login_
# Create your views here.

from .forms import AuthForm


def login(request):
    print(request.method)
    if request.method == 'GET':
        form = AuthForm()
        return render(
        request,
        'users/login.html',
        {
            'form': form,
        }
    )
    else:
        return HttpResponse('not av.')


def logout(request):
    return HttpResponse

