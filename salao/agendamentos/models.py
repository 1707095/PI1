from django.db import models

# Create your models here.
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

# Configuração do banco de dados SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite3'),
    }
}

# Modelo de Usuário (Cliente e Profissional)
class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('cliente', 'Cliente'),
        ('profissional', 'Profissional'),
        ('administrador', 'Administrador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='cliente')
    telefone = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)


# Modelo de Profissional
class Profissional(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='profissionais/', blank=True, null=True)

    def __str__(self):
        return f"{self.usuario}"


# Modelo de Serviço
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.IntegerField()  # Duração em minutos
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome}"

# Relacionamento entre Profissional e Serviço
class ProfissionalServico(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

# Modelo de Agendamento
class Agendamento(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    )
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo': 'cliente'})
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.profissional} | {self.servico} | {self.data_hora}"

# Modelo de Horários de Trabalho do Profissional
class HorarioTrabalho(models.Model):
    DIAS_SEMANA = (
        ('domingo', 'Domingo'),
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
    )
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

# # Modelo de Pagamento
# class Pagamento(models.Model):
#     FORMA_PAGAMENTO = (
#         ('cartao', 'Cartão'),
#         ('dinheiro', 'Dinheiro'),
#         ('pix', 'PIX'),
#         ('boleto', 'Boleto'),
#         ('outro', 'Outro'),
#     )
#     STATUS_PAGAMENTO = (
#         ('pendente', 'Pendente'),
#         ('pago', 'Pago'),
#         ('cancelado', 'Cancelado'),
#     )
#     agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
#     valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
#     forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO)
#     status = models.CharField(max_length=20, choices=STATUS_PAGAMENTO, default='pendente')
#     data_pagamento = models.DateTimeField(blank=True, null=True)

# # Modelo de Avaliação
# class Avaliacao(models.Model):
#     cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
#     nota = models.IntegerField()
#     comentario = models.TextField(blank=True, null=True)
#     data_avaliacao = models.DateTimeField(auto_now_add=True)

# # Comando para rodar as migrações
# # ios.system("python manage.py makemigrations")
# # ios.system("python manage.py migrate")

