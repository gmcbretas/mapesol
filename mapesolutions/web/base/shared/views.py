from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .filters import *
import json
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from django.core.serializers import serialize

class ConsultaViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """

    queryset = Consulta.objects.annotate(gasto=Coalesce(Sum('exame__valor'),0),qtd_exames=Count('exame')).order_by('gasto').all()
    serializer_class = ConsultaSerializer
    filter_class = ConsultaFilter

class ExameViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = Consulta.objects.values('medico_id','nome_medico').distinct().order_by('nome_medico')
    serializer_class = MedicoSerializer

def main(request):

    return render(request, "main.html",
                  {'shapefiles': "shapefiles"})