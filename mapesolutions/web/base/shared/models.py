from django.db.models import Model, ForeignKey, CharField, IntegerField, FloatField, DateField, CASCADE


class Consulta(Model):
    medico_id = IntegerField()
    nome_medico = CharField(max_length=50)
    data = DateField()
    valor = FloatField()



class Exame(Model):
    tipo = IntegerField()
    consulta = ForeignKey(Consulta,on_delete=CASCADE)
    valor = FloatField()


