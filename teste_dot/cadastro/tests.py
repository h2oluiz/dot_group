from datetime import date

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Livro

# Create your tests here.


class LivrariaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_livro_list = reverse("listar-livros")
        self.url_livro_cadastro = reverse("livro-cadastro")

    @classmethod
    def setUpTestData(cls):
        """
        Iniciando dados como base do test
        """

        livros = [
            {
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis",
                "data_publicacao": "1899-01-01",
                "resumo": "Romance clássico que narra a vida de Bentinho e a dúvida sobre Capitu.",
            },
            {
                "titulo": "Grande Sertão: Veredas",
                "autor": "João Guimarães Rosa",
                "data_publicacao": "1956-01-01",
                "resumo": "A jornada de Riobaldo pelo sertão e sua ligação com Diadorim.",
            },
            {
                "titulo": "Capitães da Areia",
                "autor": "Jorge Amado",
                "data_publicacao": "1937-01-01",
                "resumo": "A história de meninos de rua de Salvador buscando sobrevivência.",
            },
        ]

        cls.livro1, cls.livro2, cls.livro3 = [Livro.objects.create(**i) for i in livros]

    def test_livros_list_endpoint(self):
        """
        GET request API endpoint
        Listar todos os livros cadastros
        """
        response = self.client.get(self.url_livro_list, format="json")

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 3)
        self.assertIn(
            self.livro1.titulo,
            [livro["titulo"] for livro in response.json()["results"]],
        )

    def test_livros_post_endpoint(self):
        """
        POST request API endpoint
        Cadastra livro na base
        """
        payload = {
            "titulo": "Livro do Luiz Santos",
            "autor": "Luiz Santos",
            "data_publicacao": "25/11/2025",
            "resumo": "Era uma vez um programador Python! Que não gostava de Java",
        }

        print(self.url_livro_cadastro)
        response = self.client.post(self.url_livro_cadastro, payload, format="json")

        # Assert the response status code and content
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["id"], 4)
