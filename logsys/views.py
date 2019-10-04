from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User


@login_required
def index(request):
    users = User.objects.all()
    return render(request, 'logsys/state_list.html', {'users': users})
