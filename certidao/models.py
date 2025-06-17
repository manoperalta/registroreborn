from django.db import models


class CertidaoNascimento(models.Model):
    # Dados da criança
    nome_crianca = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')])
    data_nascimento = models.DateField()
    hora_nascimento = models.TimeField()
    local_nascimento = models.CharField(max_length=255)
    dnv = models.CharField("Declaração de Nascido Vivo", max_length=50, unique=True)

    # Dados da mãe
    nome_mae = models.CharField(max_length=255)
    nacionalidade_mae = models.CharField(max_length=100)
    naturalidade_mae = models.CharField(max_length=100)
    idade_mae = models.PositiveIntegerField()
    profissao_mae = models.CharField(max_length=100, blank=True, null=True)
    endereco_mae = models.TextField()

    # Dados do pai (opcional)
    nome_pai = models.CharField(max_length=255, blank=True, null=True)
    nacionalidade_pai = models.CharField(max_length=100, blank=True, null=True)
    naturalidade_pai = models.CharField(max_length=100, blank=True, null=True)
    idade_pai = models.PositiveIntegerField(blank=True, null=True)
    profissao_pai = models.CharField(max_length=100, blank=True, null=True)
    endereco_pai = models.TextField(blank=True, null=True)

    # Avós maternos e paternos
    nome_avo_materno = models.CharField(max_length=255, blank=True, null=True)
    nome_avo_materna = models.CharField(max_length=255, blank=True, null=True)
    nome_avo_paterno = models.CharField(max_length=255, blank=True, null=True)
    nome_avo_paterna = models.CharField(max_length=255, blank=True, null=True)

    # Estado civil dos pais
    estado_civil_pais = models.CharField(
        max_length=50,
        choices=[
            ('Casados', 'Casados'),
            ('União Estável', 'União Estável'),
            ('Solteiros', 'Solteiros'),
            ('Separados', 'Separados'),
            ('Divorciados', 'Divorciados'),
            ('Outros', 'Outros'),
        ],
        blank=True,
        null=True
    )

    # Dados do registro
    data_registro = models.DateField(auto_now_add=True)
    livro = models.CharField(max_length=20)
    folha = models.CharField(max_length=20)
    termo = models.CharField(max_length=20)
    nome_oficial_cartorio = models.CharField(max_length=255)
    
    # Declarante (pode ser a mãe, pai ou outro responsável)
    nome_declarante = models.CharField(max_length=255)

    def __str__(self):
        return f"Certidão de {self.nome_crianca} - Livro {self.livro}, Folha {self.folha}, Termo {self.termo}"
    def pdf_url(self):
        return f"/media/certidoes/certidao_{self.id}.pdf"
