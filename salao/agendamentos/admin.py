from django.contrib import admin

# Register your models here.
from .models import Usuario, Profissional, Agendamento, HorarioTrabalho, Servico;

admin.site.register(Usuario)
admin.site.register(Profissional)
admin.site.register(Agendamento)
admin.site.register(HorarioTrabalho)
admin.site.register(Servico)