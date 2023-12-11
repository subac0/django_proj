from django.shortcuts import render, redirect

from .forms import VooForm
from .models import Voo

def home(request):
    return render(request, 'reservas/home.html')

def listar(request):
    query = request.GET.get('search')
    search_type = request.GET.get('search_type', 'nome')

    listagem = Voo.objects.all().order_by('numero_voo')

    if query:
        if search_type == 'nome':
            listagem = listagem.filter(nome__icontains=query)
        if search_type == 'numero_voo':
            listagem = listagem.filter(numero_voo__icontains=query)
        if search_type == 'classe':
            listagem = listagem.filter(classe__icontains=query)

    context = {
        'dados': listagem
    }

    return render(request, 'reservas/listar.html', context)

def reservar(request):
    form = VooForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('listar')

    context = {
        'form': form,
    }

    return render(request, 'reservas/reservar.html', context)

def editar(request, voo_pk):
    dados = Voo.objects.get(pk=voo_pk)

    form = VooForm(request.POST or None, instance=dados)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('listar')

    context = {
        'form': form,
        'id':voo_pk,
    }

    return render(request, 'reservas/editar.html', context)

def deletar(request, voo_pk):
    dados = Voo.objects.get(pk=voo_pk)

    dados.delete()

    return redirect('listar')