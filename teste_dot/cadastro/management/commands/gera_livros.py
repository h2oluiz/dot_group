import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from mimesis import Generic
from mimesis.locales import Locale

from cadastro.models import Livro


class Command(BaseCommand):
    help = "Gera base com Livros"

    def handle(self, *args, **kwargs):
        generator = Generic(locale=Locale.PT_BR)
        for _ in range(30):
            livro = {
                "titulo": generator.text.title(),
                "autor": generator.person.full_name(),
                "data_publicacao": f"{generator.datetime.year()}-01-01",
                "resumo": generator.text.text(quantity=3),
            }

            Livro.objects.create(**livro)
            self.stdout.write("livro %s" % livro["titulo"])
