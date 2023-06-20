import mercadopago
import json

CLIENT_ID = '1981500552075573'
CLIENT_SECRET = 'LzUzvCM8gc7ZZBskSe3oQRZFYwVXRJ05'


def payment(req, **kwargs):
    product = kwargs['product']
    preference = {
      "items": [
        {
          "title": product.name,
          "quantity": product.quantity,
          "currency_id": "BRL",
          "unit_price": product.price
        }
      ]
    }

    mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url
