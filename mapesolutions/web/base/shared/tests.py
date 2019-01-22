from django.test import TestCase

from rest_framework.test import APIRequestFactory
import datetime

from .views import *
from django.core.management import call_command


class ConsultaTest(TestCase):

    def setUp(self):
        call_command("loaddata", "consulta", verbosity=1)
        call_command("loaddata", "exame", verbosity=1)

    def test_medico_filter(self):
        request = APIRequestFactory().get("",{'format': 'json','medico':'José Ramos'})
        consultas = ConsultaViewSet.as_view({'get': 'list'})
        response = consultas(request)
        errors=0
        for consulta in response.data:
            if consulta["nome_medico"] != 'José Ramos':
                errors += 1

        self.assertEqual(errors, 0)
        self.assertEqual(response.status_code, 200)

    def test_data_filter(self):
        date_str = '03/07/2017'  # The date
        request = APIRequestFactory().get("", {'format': 'json', 'data_0': date_str,'data_1': date_str})
        consultas = ConsultaViewSet.as_view({'get': 'list'})
        response = consultas(request)

        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(date_str, format_str)
        data = str(datetime_obj.date())

        errors = 0
        for consulta in response.data:
            if consulta["data"] != data:
                errors += 1
        self.assertEqual(errors, 0)
        self.assertEqual(response.status_code, 200)

