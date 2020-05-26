#! /usr/bin/env python3
# coding : utf-8
import pytest
import requests
from .env import KEY
# from models.googlemapsapi import GoogleAPI

class GoogleMaps:

    def __init__(self):

        self.url = "https://maps.googleapis.com/maps/api/geocode/json?"

        self.params = {
            "address": adress,
            "key": KEY
            }
def get_adress(location):
    """ returns coordinates with lat and longitude"""
    pass


def test_get_location_address(monkeypatch):
    lat, lng = locations = ["latitude", "longitude"]

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return {
                "locations": [{"coordinates": location} for location in locations]}
    monkeypatch.setattr("requests.get", MockRequestsGet)

    assert get_address(len(locations)) == locations

# def test_get_pizzas_returns_correct_names(monkeypatch):
#     product1, product2 = products = ['My product 1', 'My product 2']
#     class MockRequestsGet:
#         def __init__(self, url, params=None):
#             pass
#         def json(self):
#             return {
#                 "products": [{"product_name": product} for product in products]
#             }

#     monkeypatch.setattr('requests.get', MockRequestsGet)

#     assert get_pizzas(len(products)) == products