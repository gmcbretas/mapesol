from django.conf.urls import url
from . import views
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'consultas', ConsultaViewSet,basename="consultas")
router.register(r'exames', ExameViewSet)
router.register(r'medicos', MedicoViewSet)


app_name = 'hello'

urlpatterns = [
    # url(r'^$', views.show_svg),
    url(r'^$', main),
    # url(r'^medicos/', medicos)

]

urlpatterns += router.urls


