# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User
from django.utils import timezone
from .slack_post import slack
import json
from datetime import date, datetime

# date, datetimeの変換関数
def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return str(obj.year) +'/'+ str(obj.month) +'/'+ str(obj.day) +'---'+ str(obj.hour) +':'+ str(obj.minute)
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))

@login_required
def index(request):
    users = User.objects.all()
    return render(request, 'logsys/state_list.html', {'users': users})

def stateupdate(request,pk):
    user = get_object_or_404(User, pk=pk)
    
    if user.login_or_out:
        user.login_or_out = False
        slack.notify(text = user.first_name+"がログアウトしました")
        user.logout_date = timezone.now()
        str = json.dumps(user.logout_date + timezone.timedelta(days=1) - timezone.timedelta(hours=15), default=json_serial)
        slack.notify(text = str)
    else:
        user.login_or_out = True
        slack.notify(text = user.first_name+"がログインしました")
        user.login_date = timezone.now()
        str = json.dumps(user.logout_date + timezone.timedelta(days=1) - timezone.timedelta(hours=15), default=json_serial)
        slack.notify(text = str)
    user.save()
    users = User.objects.all()
    return render(request, 'logsys/state_list.html', {'users': users})

