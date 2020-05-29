'''
ANTES

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from .models import Jogo
from .serializers import JogosSerializer


class JogoApiView(ListAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogosSerializer

class JogosCreateView(CreateAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogosSerializer

class JogosUpdateView(UpdateAPIView):
    queryset = Jogo.objects.all().select_related('categoria')
    serializer_class = JogosSerializer


jogos_view = JogoApiView.as_view()
jogos_create_view = JogosCreateView.as_view()
jogos_update_view = JogosUpdateView.as_view()

'''
from .models import Jogo, Categoria
from .serializers import JogosSerializer, CategoriaSerializer

from rest_framework import viewsets

class JogosViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogosSerializer
    categoria = CategoriaSerializer()
