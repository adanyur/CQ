from django.conf.urls import url
from .views.intervencion import *
from .views.anestesia import *
from .views.disponibilidad_salas import *

urlpatterns = [
    url(r'^anestesia', anestesia_api_view),
    url(r'^intervencion', intervencion_api_view),
    url(r'^sala', disponibilidad_salas_api_view),
]