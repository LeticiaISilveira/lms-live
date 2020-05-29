from django.urls import path

from restrito import views

app_name = 'restrito'
urlpatterns = [
    path('', views.home, name='home'),
    path('novo-curso', views.curso_form, name='curso-form')
]
