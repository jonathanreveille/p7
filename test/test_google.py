#! /usr/bin/env python3
# coding : utf-8

import pytest
import requests
import requests_mock
from models.googlemapsapi import GoogleMaps

def test_get_json():
    g = GoogleMaps("Le Louvres")
    assert type(g.get_json()) == dict

def test_get_geocode():
    g = GoogleMaps("Le Louvres")
    g.get_json()
    assert g.get_geocode() == {'lat': 48.8606111, 'lng': 2.337644}

def test_mock_api(requests_mock):
    requests_mock.get("http://test.com", text="data")
    assert "data" == requests.get('http://test.com').text

    
def test_get_response(monkeypatch):
    lat, lng = locations = ["lat: 48.8606111", "lng: 2.337644"]
    
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
        def json(self):
            return {
                "locations": [{"position" : position} for position in locations]
            }

    monkeypatch.setattr("requests.get", MockRequestsGet)
    g = GoogleMaps("Le Louvres")

    assert g.get_geocode(len(locations)) == locations


    