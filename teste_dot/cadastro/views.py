from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Livro
from .serializers import LivroSerializer


class LivroCreate(generics.CreateAPIView):
    """
    Cadastra Livro.
    """

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class LivroList(generics.ListAPIView):
    """
    Retorna todos os Livros cadastrados.
    """

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["titulo", "autor"]


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retorna detalhes do Livro especificado por ID.
    """

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_object(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(Livro, id=pk)
