from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from catalogos.forms import LivroForm

from catalogos.models import Livro

@login_required
def template(request):
    return render(request, 'base.html', {})

@login_required
def listar(request):
    catalogos = Livro.objects.all()

    eh_professor = request.user.groups.filter(name='Professor').exists()


    
    context = {
        "catalogos": catalogos
    }
    return render(request, 'catalogos/listar.html', context)

#def MeusLivros(request):
   

@login_required
def detail(request, livro_id):
    catalogos = Livro.objects.get(pk=livro_id)    
    context = {
        "catalogos": catalogos
    }
    return render(request, 'catalogos/detail.html', context)

@login_required
def criar(request):
    
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/catalogos")
    else:
        form = LivroForm()
    
    context ={
        'form': form
    }
    
    return render(request, "catalogos/formCriar.html", context)

@login_required
def excluir(request, livro_id):
    
    Livro.objects.get(pk=livro_id).delete()
    
    return HttpResponseRedirect("/catalogos")    


def editar(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)
    
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/catalogos")
    else:
        form = LivroForm(instance=livro)
    
    context ={
        'form': form,
        'livro_id': livro_id
    }
    
    return render(request, "catalogos/formEditar.html", context)



