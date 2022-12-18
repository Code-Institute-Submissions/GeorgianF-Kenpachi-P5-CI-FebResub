import json
from store.models import Product


def cookie_cart(request):
    # for user that are not authenticated
    try:
        bag = json.loads(request.COOKIES['cart'])
        print(bag)
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
