from rest_framework import viewsets
from rest_framework.filters import SearchFilter  # Importando corretamente o filtro
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]  # Aqui está o erro corrigido
    search_fields = ['username']  # Permite buscar pelo nome do usuário