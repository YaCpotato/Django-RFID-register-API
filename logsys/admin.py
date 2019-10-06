from django.contrib import admin
from .models import User,ufid,logger
# Register your models here.
admin.site.register(User)
admin.site.register(ufid)
admin.site.register(logger)