from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
    path('profissionais/', views.listar_profissionais, name='listar_profissionais'),
    path('profissionais/adicionar/', views.adicionar_profissional, name='adicionar_profissional'),
    path('profissionais/<int:pk>/', views.listar_profissionais, name='editar_profissional'),
    path('profissionais/excluir/<int:pk>/', views.excluir_profissional, name='excluir_profissional'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamentos/excluir/<int:pk>/', views.excluir_agendamento, name='deletar_agendamento'),  # <- ESTE aqui
]

