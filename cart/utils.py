import json
from store.models import Product
from checkout.models import Order


def cookie_cart(request):
    # for user that are not authenticated
    try:
        bag = json.loads(request.COOKIES['cart'])
    except KeyError:
        bag = {}

    # define the empty cart
    items = []
    order = {
        'get_cart_total': 0,
        'get_cart_items': 0,
        }
    cart_items = order['get_cart_items']

    for i in bag:
        cart_items += int(bag[i]['quantity'])
        product = Product.objects.get(id=i)
        total = (product.price * bag[i]['quantity'])

        order['get_cart_total'] += total
        order['get_cart_items'] += bag[i]['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'imageURL': product.imageURL
                },
            'quantity': bag[i]['quantity'],
            'get_total': total,
        }
        
        items.append(item)

    return {
        'cart_items': cart_items,
        'order': order,
        'items': items
        }


def cart_details(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        cookie_info = cookie_cart(request)
        cart_items = cookie_info['cart_items']
        order = cookie_info['order']
        items = cookie_info['items']

    return {
        'cart_items': cart_items,
        'order': order,
        'items': items
    }
