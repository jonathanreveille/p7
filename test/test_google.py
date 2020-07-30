#! /usr/bin/env python3
# coding : utf-8

# import pytest
from models.googlemapsapi import GoogleMaps


def test_get_json():
    """ we will if output is dictionary type"""
    g = GoogleMaps("Tour Eiffel")
    assert isinstance(g.get_json_test(), dict)


def test_get_geocode():
    """ we will test if we the right coordinates
    from a place"""
    g = GoogleMaps("Le Louvres")
    g.get_json_test()
    assert g.get_geocode_test() == {'lat': 48.8606111, 'lng': 2.337644}


def test_google_api_response(monkeypatch):
    IMITATION_RESPONSE = {'locations': [{'Position': 'Position'}]}
    # ^Remplacer par la structure de donnée désirée

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass

        def json(self):
            return IMITATION_RESPONSE

    response = MockRequestsGet
    path = "models.googlemapsapi.GoogleMaps.get_json_test"
    monkeypatch.setattr(path, response.json)

    assert response.json(IMITATION_RESPONSE) == IMITATION_RESPONSE


#########################################################
#########################################################
#########################################################
# #
# import requests_mock

# def test_mock_api(requests_mock):
#     requests_mock.get("http://test.com", text="data")
#     assert "data" == requests.get('http://test.com').text

# def test_get_response(monkeypatch):
#     response = {'locations': [{'Position': 'locations'}]}

#     class MockRequestsGet:
#         def __init__(self, url, params=None):
#             self.status_code = 200
#         def json(self):
#             return {
#                 "locations": [{"Position" : position} for position in response]}

#     monkeypatch.setattr("requests.get", MockRequestsGet)
#     g = GoogleMaps("Louvres")
#     assert g.get_json() == response
#     #{'locations': [{'Position': 'lat: 48.8606111'}, {'Position': 'lng: 2.337644'}]}


# def mock_geocode():
#     responses = {"location":[{"Position":"lat", "Position":"lng"}]}
#     return responses

# def test_get_response_from_an_api(monkeypatch):
#     lat, lng = responses = {"location":[{"Position":"lat", "Position":"lng"}]}

#     class MockRequestsGet:

#         def __init__(self, url, params=None):
#             self.status_code = 200
#         def json(self):
#             return {
#                 "location": [{"Position": lat} for lat, lng in responses}]

#     monkeypatch.setattr("models.googlemapsapi.get_geocode",  MockRequestsGet)
#     assert mock_geocode(responses) == responses
