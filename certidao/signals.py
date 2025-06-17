import os
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
from .models import CertidaoNascimento
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CertidaoNascimento)
def certidaonascimento_post_save(sender, instance, **kwargs):
    # Renderiza HTML com os dados da certidão
    html_string = render_to_string('certidao/certidao_nascimento.html', {'certidao': instance})
    
    # Define caminho para salvar o PDF
    output_dir = os.path.join(settings.MEDIA_ROOT, 'certidoes')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'certidao_{instance.id}.pdf')
    
    # Gera o PDF com WeasyPrint
    HTML(string=html_string).write_pdf(output_path)

