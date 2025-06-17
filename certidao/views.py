from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .models import CertidaoNascimento
from .forms import CertidaoNascimentoForm


# Criação da certidão
class CertidaoNascimentoCreateView(CreateView):
    model = CertidaoNascimento
    form_class = CertidaoNascimentoForm
    template_name = 'certidao_form.html'
    success_url = reverse_lazy('certidao_list')

# Visualização detalhada
class CertidaoNascimentoDetailView(DetailView):
    model = CertidaoNascimento
    template_name = 'certidao_detail.html'
    context_object_name = 'certidao'

# Lista de certidões
class CertidaoNascimentoListView(ListView):
    model = CertidaoNascimento
    template_name = 'certidao_list.html'
    context_object_name = 'certidoes'

