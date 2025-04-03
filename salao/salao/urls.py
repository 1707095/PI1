from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agendamentos import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)  # Cria as rotas automaticamente

urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas do DRF
    path('views/', views.current_datetime),
]