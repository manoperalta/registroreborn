from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','product_name', 'price', 'status', 'mercadopago_payment_id', 'created_at', 'updated_at')