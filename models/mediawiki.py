# #! /usr/bin/env python3
# # coding : utf-8

# import pytest

# def test_mediawiki_api(monkeypatch):
#     IMITATION_RESPONSE_2 = {'batchcomplete': '',
#                                 'query': {'geosearch': [{'dist': 129.9,
#                                 'lat': 37.78785,
#                                 'lon': -122.40065,
#                                 'ns': 0,
#                                 'pageid': 6422233,
#                                 'primary': '',
#                                 'title': 'Academy of Art University'}}}

#     class MockRequestsGet():
#         """Class that mocks the call to the API and
#         gets json result in output"""
#         def __init__(self, url, params=None):
#             pass
#         def json(self):
#             return IMITATION_RESPONSE_2

    
#     response =  MockRequestsGet
#     path = "models.mediawiki.MediaWiki.get_json"
#     monkeypatch.setattr(path, response.json)



# # def test_google_api_response(monkeypatch):         
# #     IMITATION_RESPONSE = {'locations': [{'Position': 'Position'}]} # Remplacer par la structure de donnée désirée
    
# #     class MockRequestsGet():
# #         def __init__(self, url, params=None):
# #             pass
# #         def json(self):
# #             return IMITATION_RESPONSE

# #     response = MockRequestsGet
# #     path = "models.googlemapsapi.GoogleMaps.get_json"
# #     monkeypatch.setattr(path, response.json)
    
# #     assert response.json(IMITATION_RESPONSE) == IMITATION_RESPONSE

# # {'batchcomplete': '',
# #  'query': {'geosearch': [{'dist': 129.9,
# #                           'lat': 37.78785,
# #                           'lon': -122.40065,
# #                           'ns': 0,
# #                           'pageid': 6422233,
# #                           'primary': '',
# #                           'title': 'Academy of Art University'},
# #                          {'dist': 140.9,
# #                           'lat': 37.788139,
# #                           'lon': -122.399056,
# #                           'ns': 0,
# #                           'pageid': 5105544,
# #                           'primary': '',
# #                           'title': '101 Second Street'},
# #                          {'dist': 163.4,
# #                           'lat': 37.7858,
# #                           'lon': -122.4008,
# #                           'ns': 0,
# #                           'pageid': 429553,
# #                           'primary': '',
# #                           'title': "Musée d'Art moderne de San Francisco"},
# #                          {'dist': 244.1,
# #                           'lat': 37.789062,
# #                           'lon': -122.398831,
# #                           'ns': 0,
# #                           'pageid': 2350884,
# #                           'primary': '',
# #                           'title': 'Golden Gate University'},
# #                          {'dist': 268.7,
# #                           'lat': 37.7854,
# #                           'lon': -122.402,
# #                           'ns': 0,
# #                           'pageid': 4644434,
# #                           'primary': '',
# #                           'title': 'Yerba Buena Center for the Arts'},
# #                          {'dist': 338,
# #                           'lat': 37.79,
# #                           'lon': -122.4,
# #                           'ns': 0,
# #                           'pageid': 3405328,
# #                           'primary': '',
# #                           'title': 'Liste des plus hautes constructions de San '
# #                                    'Francisco'},
# #                          {'dist': 369.6,
# #                           'lat': 37.7842,
# #                           'lon': -122.402,
# #                           'ns': 0,
# #                           'pageid': 3935225,
# #                           'primary': '',
# #                           'title': 'Moscone Center'},
# #                          {'dist': 384.3,
# #                           'lat': 37.7903,
# #                           'lon': -122.3985,
# #                           'ns': 0,
# #                           'pageid': 11091020,
# #                           'primary': '',
# #                           'title': 'Oceanwide Center'},
# #                          {'dist': 384.7,
# #                           'lat': 37.788688,
# #                           'lon': -122.403477,
# #                           'ns': 0,
# #                           'pageid': 9025323,
# #                           'primary': '',
# #                           'title': '88 Kearny Street'},
# #                          {'dist': 401.6,
# #                           'lat': 37.7858,
# #                           'lon': -122.404,
# #                           'ns': 0,
# #                           'pageid': 9902380,
# #                           'primary': '',
# #                           'title': 'Contemporary Jewish Museum'}]}}
