import json
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, ShippingAddress
import stripe


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLIC_KEY
            }
        print(stripe_config)
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://georgianf-kenpachip5ci-l5z6xtwb420.ws-eu77.gitpod.io/' # need to change to production 
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Katana',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '100',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0
            }
        cart_items = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }
    return render(request, 'checkout/checkout.html', context)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            country=data['shipping']['country'],
        )

    else:
        print('User is not logged in')

    return JsonResponse('Transaction complete!', safe=False)
