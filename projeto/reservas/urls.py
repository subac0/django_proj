from django.urls import path,include
from .views import home, reservar, listar, editar, deletar

urlpatterns = [
    path('', home, name='home'),
    path('reservar/', reservar, name='reservar'),
    path('listar/', listar, name='listar'),
    path('reservar/edit/<int:voo_pk>', editar, name='editar'),
    path('reservar/delete/<int:voo_pk>', deletar, name='deletar')
]