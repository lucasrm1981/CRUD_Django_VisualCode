from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    vidade= request.POST.get("idade")
    Pessoa.objects.create(nome=vnome, idade=vidade)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa":pessoa})
        
def update(request, id):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.idade = vidade
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)