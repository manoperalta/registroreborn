from django.urls import path
from .views import CreatePaymentView, payment_webhook, product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', CreatePaymentView.as_view(), name='create_payment'),
    path('webhook/', payment_webhook, name='payment_webhook'),
]
