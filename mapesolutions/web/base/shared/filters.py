import django_filters as filters
from .models import *
# Create your views here.

class ConsultaFilter(filters.FilterSet):
    data = filters.DateFromToRangeFilter(field_name='data')
    # First field - from
    data.field.fields[0].input_formats = ['%d/%m/%Y']
    # Last field - to
    data.field.fields[-1].input_formats = ['%d/%m/%Y']


    medico = filters.CharFilter(name='nome_medico',lookup_expr='icontains')


    class Meta:
        model = Consulta
        fields = {'data','nome_medico'}
