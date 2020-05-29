from .models import Jogo, Categoria
from rest_framework import serializers



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        #fields = ['categoria']
        fields = '__all__'
        



class JogosSerializer(serializers.ModelSerializer):
    disponivel = serializers.ReadOnlyField()
    #categoria = CategoriaSerializer()
    class Meta:
        model = Jogo
        exclude = ['estoque', 'id']




