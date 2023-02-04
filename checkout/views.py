import json
import datetime
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import stripe
from store.models import Customer
from cart.utils import cart_details
from .models import Order, OrderItem, ShippingAddress
from store.models import Product


@csrf_exempt
def stripe_config(request):
    """
    A view to configure Stripe
    """
    if request.method == 'GET':
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLIC_KEY
            }
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """
    A view to create a checkout session in Stripe
    and collect the shipping details
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    domain_url = 'https://kenpachi-estore.herokuapp.com/checkout/'
    success_url = 'success?session_id={CHECKOUT_SESSION_ID}'
    cart_info = cart_details(request)
    order = cart_info['order']

    if request.user.is_authenticated:
        customer = request.user.customer
        customer.email = request.user.email
        customer.save()

    if request.method == 'GET':
        checkout_session = stripe.checkout.Session.create(
            shipping_address_collection={
                "allowed_countries":
                    ["US", "CA", "NL", "GB"]
                },
            client_reference_id=request.user.id,
            customer_email=customer.email,
            success_url=domain_url + success_url,
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


@csrf_exempt
def stripe_webhook(request):
    """
    A view to handle the Stripe Webhook and process the order
    """
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
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )

        transaction_id = datetime.datetime.now().timestamp()
        total = session['amount_total']
        customer_email = session['customer_email']
        web_domain = 'https://kenpachi-estore.herokuapp.com/'
        customer = Customer.objects.get(email=customer_email)
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
        shipping_details = get_object_or_404(ShippingAddress, order=order)

        # Decrease the stock
        order_items = OrderItem.objects.filter(order=order)
        for item in order_items:
            product = Product.objects.get(id=item.product.id)
            product.stock -= item.quantity
            product.save()

        # Send confirmation email
        sender = settings.EMAIL_HOST_USER
        message = (
                f"Hey there {customer}," +
                "\n\n" +
                "Congratulations on your purchase!" +
                "\n\n" +
                "Below you can find the order details:" +
                "\n\n" +
                f"Order Number: {order.transaction_id}" +
                "\n" +
                f"Order Total: ${total/100}0" +
                "\n" +
                f"Order Date: {order.date_ordered}" +
                "\n\n" +
                "Shipping details:" +
                "\n"
                f"Address: {shipping_details.address}" +
                "\n"
                f"City: {shipping_details.city}" +
                "\n"
                f"Postcode: {shipping_details.zipcode}" +
                "\n"
                f"Country: {shipping_details.country}" +
                "\n" +
                "\n" +
                "Your ordered item(s) will arrive shortly" +
                "\n" +
                f"For more information on the order, go to {web_domain}"
                "\n" +
                "\n" +
                "Kenpachi Team"
                )
        send_mail(
            '[Kenpachi eStore] Order confirmation',
            message,
            sender,
            [customer_email],
            fail_silently=False,
        )
        return JsonResponse('Checkout Complete!', safe=False)


def success(request):
    """
    A view to redirect if the order is processed
    """
    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }
    return render(request, 'checkout/success.html', context)


def cancelled(request):
    """
    A view to redirect if the order is cancelled
    """
    cart_info = cart_details(request)

    cart_items = cart_info['cart_items']
    order = cart_info['order']
    items = cart_info['items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }
    return render(request, 'checkout/cancelled.html', context)


def checkout(request):
    """
    A view to render the checkout page with the cart items
    """
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
