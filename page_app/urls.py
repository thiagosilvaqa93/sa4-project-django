from django.urls import path
from page_app.views import index, contato, services

urlpatterns = [
    path('', index), # URL padrão que direciona para a view index

    path('contato/', contato), # URL que direciona para a view contato

    path('services/', services), # URL que direciona para a view contato
]
