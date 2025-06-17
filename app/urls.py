from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from certidao.views import (
    CertidaoNascimentoCreateView,
    CertidaoNascimentoDetailView,
    CertidaoNascimentoListView,
    
)
from accounts.views import register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('nova/', CertidaoNascimentoCreateView.as_view(), name='certidao_create'),
    path('<int:pk>/', CertidaoNascimentoDetailView.as_view(), name='certidao_detail'),
    path('', CertidaoNascimentoListView.as_view(), name='certidao_list'),
    
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
