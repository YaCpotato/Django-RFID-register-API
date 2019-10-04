from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User
from django.utils import timezone

@login_required
def index(request):
    users = User.objects.all()
    return render(request, 'logsys/state_list.html', {'users': users})

def stateupdate(request,pk):
    user = get_object_or_404(User, pk=pk)
    
    if user.login_or_out:
        user.login_or_out = False
        user.logout_date = timezone.now()
    else:
        user.login_or_out = True
        user.login_date = timezone.now()
    user.save()
    users = User.objects.all()
    return render(request, 'logsys/state_list.html', {'users': users})

