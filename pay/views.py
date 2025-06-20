import json
import mercadopago
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Payment
from django.contrib.auth.models import User
from django.shortcuts import render

def product_list(request):
    return render(request, 'pay/products.html')


# Configure sua chave correta aqui
sdk = mercadopago.SDK(
    "TEST-10722434116df95782-09f3023-00095cb15433988cb42b938b232f25893e6-43916148"
)


class CreatePaymentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        # Valida campos obrigatórios
        if not all(k in data for k in ("user_id", "product_name", "price")):
            return JsonResponse({"error": "Campos obrigatórios ausentes"}, status=400)

        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuário não encontrado"}, status=404)

        # Cria o pagamento no banco
        payment = Payment.objects.create(
            user=user,
            product_name=data['product_name'],
            price=data['price'],
        )

        # Dados para o MercadoPago
        preference_data = {
            "items": [{
                "title": payment.product_name,
                "quantity": 1,
                "unit_price": float(payment.price),
                "currency_id": "BRL",
            }],
            "notification_url": request.build_absolute_uri("/pay/webhook/"),
            "external_reference": str(payment.id),
        }

        preference_response = sdk.preference().create(preference_data)

        # Logar resposta para depuração
        print("Preference response:", preference_response)

        response_body = preference_response.get("response", {})
        init_point = response_body.get("init_point")

        if init_point:
            return JsonResponse({"init_point": init_point})
        else:
            return JsonResponse(
                {"error": "Erro ao criar pagamento", "detalhes": response_body},
                status=400
            )


@csrf_exempt
def payment_webhook(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        if "data" in body and "id" in body["data"]:
            mp_payment_id = body["data"]["id"]

            # Obtém detalhes do pagamento
            payment_info = sdk.payment().get(mp_payment_id)
            response_body = payment_info.get("response", {})
            external_reference = response_body.get("external_reference")
            status = response_body.get("status")

            if not external_reference:
                return HttpResponse(status=400)

            try:
                payment = Payment.objects.get(id=external_reference)
                payment.status = status
                payment.mercadopago_payment_id = mp_payment_id
                payment.save()
            except Payment.DoesNotExist:
                pass

        return HttpResponse(status=200)

    return HttpResponse(status=405)
