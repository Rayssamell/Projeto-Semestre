from django.contrib import admin

from .models import Livro, Disciplina, Avaliacao

admin.site.register(Livro)
admin.site.register(Disciplina)
admin.site.register(Avaliacao)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('livro', 'docente', 'id')
        }),
        ('Avaliacao', {
            'fields': ('status', 'due_back')
        }),
    )