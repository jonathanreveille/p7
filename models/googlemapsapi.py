#! /usr/bin/env python3
# coding : utf-8

import requests

class GoogleAPI:

    def __init__(self):
        pass

    def get_address(self):
        pass


# def get_pizzas(quantity):
    
#     """Returns a list of pizza names."""
#     payload = {
#         "action": "process",
#         "json": 1,
#         "tagtype_0": "categories",
#         "tag_contains_0": "contains",
#         "tag_0": "pizzas",
#         "page_size": quantity if quantity < 1000 else 1000
#     }
#     response = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',params=payload
#     )
#     products = response.json()['products']

#     return [product['product_name'] for product in products if 'product_name' in product]



