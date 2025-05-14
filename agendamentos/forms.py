from django import forms
from .models import Cliente, Profissional, Agendamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'rg', 'nome', 'social', 'sexo', 'data_nascimento', 'email',
            'telefone_residencial', 'telefone_celular', 'endereco',
            'bairro', 'cidade', 'cep', 'ultimo_atendimento', 'data_ativo'
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'ultimo_atendimento': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'rg', 'cpf', 'nome', 'data_nascimento', 'email', 'telefone_residencial',
            'telefone_celular', 'endereco', 'bairro', 'cidade', 'cep',
            'habilidades_profissionais'
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = [
            'data_agendado', 'horario', 'cliente', 'profissional',
            'servicos', 'observacoes', 'valor_previsto'
        ]
        widgets = {
            'data_agendado': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }
