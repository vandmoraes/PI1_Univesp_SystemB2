from django.db import models

class Cliente(models.Model):
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    social = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone_residencial = models.CharField(max_length=20, blank=True, null=True)
    telefone_celular = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    historico = models.TextField(blank=True, null=True)
    ultimo_atendimento = models.DateField(blank=True, null=True)
    data_ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone_residencial = models.CharField(max_length=20, blank=True, null=True)
    telefone_celular = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    habilidades_profissionais = models.TextField(blank=True, null=True)
    apontamentos = models.TextField(blank=True, null=True)
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    data_solicitado = models.DateTimeField(auto_now_add=True, verbose_name="Data da Solicitação")
    data_agendado = models.DateField(verbose_name="Data Agendada")
    horario = models.TimeField(verbose_name="Horário")
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name="Cliente")
    profissional = models.ForeignKey('Profissional', on_delete=models.CASCADE, verbose_name="Profissional")
    servicos = models.TextField(verbose_name="Serviços")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    valor_previsto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Valor Previsto (R$)")

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ['-data_solicitado']  # ordena do mais recente para o mais antigo

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_agendado.strftime('%d/%m/%Y')} às {self.horario.strftime('%H:%M')}"