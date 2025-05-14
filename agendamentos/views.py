from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Profissional, Agendamento
from .forms import ClienteForm, ProfissionalForm, AgendamentoForm
from django.utils import timezone


def home(request):
    hoje = timezone.now().date()
    agendamentos = Agendamento.objects.filter(data_agendado__gte=hoje).order_by('data_agendado', 'horario')
    return render(request, 'home.html', {'agendamentos': agendamentos})


def listar_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'form': form, 'clientes': clientes})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'adicionar_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'listar_clientes.html', {'form': form})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('listar_clientes')

def listar_profissionais(request, pk=None):
    if pk:
        profissional = get_object_or_404(Profissional, pk=pk)
    else:
        profissional = None

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm(instance=profissional)

    profissionais = Profissional.objects.all()
    return render(request, 'listar_profissionais.html', {'form': form, 'profissionais': profissionais})

def adicionar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm()
    return render(request, 'adicionar_profissional.html', {'form': form})

def editar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm(instance=profissional)
    return render(request, 'editar_profissional.html', {'form': form})

def excluir_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    profissional.delete()
    return redirect('listar_profissionais')


def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('-data_solicitado')  # Agendamentos ordenados do mais recente para o mais antigo
    form = AgendamentoForm()

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.data_solicitado = timezone.now()  # Salva a data da solicitação no momento do cadastro
            agendamento.save()
            return redirect('listar_agendamentos')

    return render(request, 'listar_agendamentos.html', {'form': form, 'agendamentos': agendamentos})

def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, 'listar_agendamentos.html', {'form': form})

def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    agendamento.delete()
    return redirect('listar_agendamentos')