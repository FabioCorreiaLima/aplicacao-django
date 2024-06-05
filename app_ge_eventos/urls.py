# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('evento/criar/', views.criar_evento, name='criar_evento'),
    path('evento/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('evento/excluir/<int:evento_id>/', views.excluir_evento, name='excluir_evento'),
]
