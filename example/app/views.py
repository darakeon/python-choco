from django.shortcuts import render
from .models import Chocolate
from .serializers import ChocolateSerializer
from rest_framework import viewsets

class ChocolateViewSet(viewsets.ModelViewSet):
    queryset = Chocolate.objects.all()
    serializer_class = ChocolateSerializer
