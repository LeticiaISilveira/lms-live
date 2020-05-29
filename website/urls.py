from django.urls import path

from website import views


app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair')
]
