from django.contrib import admin
from .models import CertidaoNascimento

@admin.register(CertidaoNascimento)
class CertidaoNascimentoAdmin(admin.ModelAdmin):
    list_display = ('nome_crianca', 'data_nascimento', 'sexo', 'nome_mae', 'nome_pai', 'livro', 'folha', 'termo', 'data_registro')
    list_filter = ('sexo', 'data_nascimento', 'estado_civil_pais', 'data_registro')
    search_fields = ('nome_crianca', 'nome_mae', 'nome_pai', 'dnv', 'livro', 'folha', 'termo')

    fieldsets = (
        ('Dados da Criança', {
            'fields': (
                'nome_crianca', 'sexo', 'data_nascimento', 'hora_nascimento', 'local_nascimento', 'dnv'
            )
        }),
        ('Dados da Mãe', {
            'fields': (
                'nome_mae', 'nacionalidade_mae', 'naturalidade_mae',
                'idade_mae', 'profissao_mae', 'endereco_mae'
            )
        }),
        ('Dados do Pai (opcional)', {
            'fields': (
                'nome_pai', 'nacionalidade_pai', 'naturalidade_pai',
                'idade_pai', 'profissao_pai', 'endereco_pai'
            )
        }),
        ('Avós', {
            'fields': (
                'nome_avo_materno', 'nome_avo_materna',
                'nome_avo_paterno', 'nome_avo_paterna'
            )
        }),
        ('Estado Civil dos Pais', {
            'fields': ('estado_civil_pais',)
        }),
        ('Registro da Certidão', {
            'fields': (
                'livro', 'folha', 'termo', 'nome_oficial_cartorio',
                'nome_declarante', 'data_registro'
            )
        }),
    )

    readonly_fields = ('data_registro',)
