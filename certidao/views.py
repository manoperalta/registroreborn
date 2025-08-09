from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .models import CertidaoNascimento
from .forms import CertidaoNascimentoForm

class CertidaoNascimentoCreateView(LoginRequiredMixin, CreateView):
    model = CertidaoNascimento
    form_class = CertidaoNascimentoForm
    template_name = 'certidao_form.html'
    success_url = reverse_lazy('certidao_list')
    login_url = reverse_lazy('login')  

class CertidaoNascimentoDetailView(LoginRequiredMixin, DetailView):
    model = CertidaoNascimento
    template_name = 'certidao_detail.html'
    context_object_name = 'certidao'
    login_url = 'login'  

class CertidaoNascimentoListView(LoginRequiredMixin, ListView):
    model = CertidaoNascimento
    template_name = 'certidao_list.html'
    context_object_name = 'certidoes'
    login_url = 'login'

