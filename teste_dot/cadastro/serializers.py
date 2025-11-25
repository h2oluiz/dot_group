from rest_framework import serializers

from .models import Livro


class LivroSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(
        read_only=True, format="%d/%m/%Y %H:%M:%S", input_formats=["%d/%m/%Y %H:%M:%S"]
    )
    update = serializers.DateTimeField(
        read_only=True, format="%d/%m/%Y %H:%M:%S", input_formats=["%d/%m/%Y %H:%M:%S"]
    )
    data_publicacao = serializers.DateField(
        format="%d/%m/%Y", input_formats=["%d/%m/%Y"]
    )

    class Meta:
        model = Livro
        fields = "__all__"
