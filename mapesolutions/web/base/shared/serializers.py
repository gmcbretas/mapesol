from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class ConsultaSerializer(serializers.HyperlinkedModelSerializer):
    gasto = serializers.FloatField()
    qtd_exames = serializers.IntegerField()
    class Meta:
        model = Consulta
        fields = ('id','nome_medico', 'data', 'valor', 'gasto','qtd_exames')


class MedicoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Consulta
        fields = ('medico_id',"nome_medico",)

class ExameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exame
        fields = ('tipo', 'valor', "consulta_id")
