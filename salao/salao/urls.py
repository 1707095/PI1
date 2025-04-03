from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agendamentos import views


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)  # Cria as rotas automaticamente


urlpatterns = [
    path('usuarios/', include(router.urls)),  # Inclui todas as rotas do DRF
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]


# Serve os arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)