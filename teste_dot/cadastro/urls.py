from django.urls import path, re_path

from .views import LivroCreate, LivroDetail, LivroList

urlpatterns = [
    path("livros/", LivroList.as_view(), name="listar-livros"),
    path("livros/cadastra/", LivroCreate.as_view(), name="livro-cadastro"),
    path("livros/<int:pk>/", LivroDetail.as_view()),
]
