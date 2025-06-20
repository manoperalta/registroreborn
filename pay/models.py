from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('aproved', ' Aprovado'),
        ('rejected', 'Rejeitado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    mercadopago_payment_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    