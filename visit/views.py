from django.shortcuts import render
from rest_framework import viewsets
from .models import Visit
from .serializer import VisitSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer