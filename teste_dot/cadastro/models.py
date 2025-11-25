from django.db import models

# Create your models here.


class Livro(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateField("data de publicação")
    resumo = models.CharField(max_length=500, blank=True, default="")

    class Meta:
        ordering = ["created"]
