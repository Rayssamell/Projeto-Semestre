from tabnanny import verbose
from django.db import models
import uuid
from datetime import date
from accounts.models import Docente 
from django.utils import timezone

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 

class Livro(models.Model):

    SERIEALVO_CHOICES = (
    ('1', ' 1° ano'),
    ('2', '2° ano'),
    ('3', '3° ano'),
    )

    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editora = models.CharField(max_length=100)
    anoPublicacao = models.IntegerField()
    isbn = models.CharField(max_length=20)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING, verbose_name="Disciplina") 
    quantidade = models.IntegerField()
    serieAlvo = models.CharField(max_length=1, choices=SERIEALVO_CHOICES, blank=True, null=False)
    imagem = models.ImageField(upload_to='images/')
    
    class Meta:
        verbose_name = 'Livros Didáticos'

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=' ID particular')
    livro = models.ForeignKey(Livro, on_delete=models.RESTRICT, null=True)
    due_back = models.DateTimeField(auto_now= True)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT, null=True)

    LOAN_STATUS = (
        ('d', 'Disponivel'),
        ('a', 'Agendado'),
        ('s', 'Solicitado'),
        ('e', 'Emprestado'),
    )

    class Meta:
        verbose_name = 'Avaliação'

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Situação do Livro',
    )


    def __str__(self):
        return f'{self.id} ({self.livro.titulo})'
