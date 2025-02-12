from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import stripe
from accounts.models import CustomUser
from shop.models import Order, OrderItem, Product, Cart
from shop.utils import get_stock, freeze_stock
from shop.utils import get_checkout_total_product

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(user, items):
    
    subtotal, delivery_charge, total = get_checkout_total_product(items)
    
    line_items = []
    for item in items:
        line_items.append({
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': item.name,
                    'images': ["https://res.cloudinary.com/dn3jtk7bz/image/upload/v1738320767/cld-sample-3.jpg"],
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        })

    try:
        checkout_session = stripe.checkout.Session.create(

            customer_email=user.email,
            payment_intent_data={
                "shipping": {
                "name": user.fullname,
                    "address": {
                        "country": "IN",
                        "state": user.address.state,
                        "city":  user.address.city,
                        "line1":  user.address.address_line,
                        "postal_code":  user.address.pincode
                    }
                }
            },

            shipping_options=[
                {
                    "shipping_rate_data": {
                        "display_name": "Delivery Charge",
                        "type": "fixed_amount",
                        "fixed_amount": {
                            "amount": delivery_charge * 100,
                            "currency": "inr"
                        },
                        "delivery_estimate": {
                            "minimum": {"unit": "day", "value": 3},
                            "maximum": {"unit": "day", "value": 5}
                        }
                    }
                }
            ],

            line_items=line_items,
            mode='payment',
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,

            metadata= {
               "user_id": user.id,
               "items": json.dumps([item.id for item in items]),
            }
        )

        return checkout_session


    except Exception as e:
        return str(e)



@csrf_exempt
def webhook_view(request):
  payload = request.body
  event = None

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), stripe.api_key
    )

  except ValueError as e:
    return HttpResponse(status=400)
  

  if event.type == 'checkout.session.completed':
    session = event['data']['object']
    user_id = session['metadata']['user_id']
    items = json.loads(session['metadata']['items'])

    user = CustomUser.objects.get(id=user_id)

    order = Order.objects.create(user=user)

    products = list(map(lambda item : Product.objects.get(id=item), items))

    for product in products:
        stock = get_stock(product=product)
        freeze_stock(stock=stock)
        OrderItem.objects.create(product=product, order=order, sku=stock)

        try:
            cart_item = Cart.objects.get(user=user, product=product)
            cart_item.delete()
        except:
           pass
        
  return HttpResponse(status=200)