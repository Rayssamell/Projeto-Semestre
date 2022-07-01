from django.urls import path

from . import views

urlpatterns = [

    path('', views.listar, name='listar'),
    path('criar/', views.criar, name='criar'),
    path('<int:livro_id>/', views.detail, name='detail'),
    path('excluir/<int:livro_id>/', views.excluir, name='excluir'),
    path('editar/<int:livro_id>/', views.editar, name='editar'),
#path('meusLivros', views.MeusLivros, name='meusLivros'),


     path('template/', views.template, name="template")

]

