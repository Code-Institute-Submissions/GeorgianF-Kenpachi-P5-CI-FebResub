import json
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from store.models import Customer
from cart.utils import cart_details
from .models import Order, ShippingAddress


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLIC_KEY
            }
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
    else:
        # TODO: add checkout session for Anonymus Users

    order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
        )
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/checkout/'
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            checkout_session = stripe.checkout.Session.create(
                shipping_address_collection={
                    "allowed_countries":
                        ["US", "CA", "NL"]
                    },
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                customer_email=request.user.email,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Kenpachi Katana Store',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': int(order.get_cart_total*100),
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({
                'error': str(e)
                })


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )

        # Fulfill the purchase...
        transaction_id = datetime.datetime.now().timestamp()
        total = session['amount_total']
        customer_id = session['client_reference_id']
        customer = Customer.objects.get(pk=customer_id)
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
        )
        order.transaction_id = transaction_id

        if (total / 100) == int(order.get_cart_total):
            order.complete = True

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=session['shipping']['address']['line1'],
            city=session['shipping']['address']['city'],
            state=session['shipping']['address']['state'],
            zipcode=session['shipping']['address']['postal_code'],
            country=session['shipping']['address']['country'],
        )

        order.save()

        # Passed signature verification
        return HttpResponse(status=200)


def success(request):
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
    return render(request, 'checkout/success.html', context)


def cancelled(request):
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
    return render(request, 'checkout/cancelled.html', context)


def checkout(request):
    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

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
