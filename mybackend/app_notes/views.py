from django.shortcuts import render

from rest_framework import viewsets

from .models import NoteModel
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = NoteModel.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
