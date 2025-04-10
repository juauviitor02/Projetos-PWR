from django.shortcuts import render
from django.http import HttpResponse
from .models import Diario, Pessoa
from django.shortcuts import redirect
from datetime import datetime, timedelta
from django.contrib import messages
# Create your views here.

def home(request):
    textos = Diario.objects.all().order_by('-criado_em')[:3]
    pessoas = Pessoa.objects.all()
    nomes = [pessoa.nome for pessoa in pessoas]
    qtds =[]
    for pessoa in pessoas:
        qtd = Diario.objects.filter(pessoas=pessoa).count()
        qtds.append(qtd)
    diarios = Diario.objects.all()
    tags = {}
    for diario in diarios:
        for tag in diario.get_tags():
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
    qtds_tags = list(tags.values())
    tag = list(tags.keys())
    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'qtds': qtds, 'qtds_tags': qtds_tags, 'tag': tag})

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        for i in pessoas:
            print(i.nome)
        return render(request, 'escrever.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')

        if len(texto.strip()) == 0 or len(titulo.strip()) == 0:
            messages.success(request, 'Texto e título são obrigatórios! Preencha-os e tente novamente.')
            return redirect('escrever')
        
        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        diario.set_tags(tags)
        diario.save()

        for i in pessoas:
            pessoa = Pessoa.objects.get(id=i)
            diario.pessoas.add(pessoa)
        diario.save()
        messages.success(request, 'Recordação salva com sucesso!')
        return redirect('home')
    

def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_pessoa.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        messages.success(request, 'Pessoa cadastrada com sucesso!')
        return redirect('home')
    
def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diario.objects.filter(criado_em__gte=data_formatada).filter(criado_em__lt=data_formatada + timedelta(days=1))
    return render(request, 'dia.html', {'diarios': diarios, 'total': len(diarios), 'data': data})

def excluir_dia(request):
    #dia = request.GET.get('data')
    dia = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(criado_em__gte=dia).filter(criado_em__lt=dia + timedelta(days=1))
    for i in diarios:
        i.delete()
    messages.success(request, 'Diários excluídos com sucesso!')
    return redirect('home')
