#! /usr/bin/env python3
# coding : utf-8

import pytest
from models.mediawiki import MediaWiki

def test_mediawiki_api_response(monkeypatch):
    """test response from the mediawiki API"""

    IMITATION_RESPONSE_MEDIAWIKI = {'batchcomplete': '',
        'query': {'geosearch': [{'dist': 129.9,
        'lat': 37.78785,
        'lon': -122.40065,
        'ns': 0,
        'pageid': 6422233,
        'primary': '',
        'title': 'Academy of Art University'}]}}
        
    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return IMITATION_RESPONSE_MEDIAWIKI
    
    response =  MockRequestsGet
    path = "models.mediawiki.MediaWiki.get_json"
    monkeypatch.setattr(path, response.json)

    assert response.json(IMITATION_RESPONSE_MEDIAWIKI) == IMITATION_RESPONSE_MEDIAWIKI


def test_get_json():
    latitude = 37.78785
    longitude = -122.40065
    mediawiki = MediaWiki(latitude,longitude)
    mediawiki.get_json()
    assert type(mediawiki.search_json) == dict


def test_get_title_from_json_object(monkeypatch):

    IMITATION_RESPONSE_MEDIAWIKI_2 = {'batchcomplete': '',
        'query': {'geosearch': [{'dist': 129.9,
        'lat': 37.78785,
        'lon': -122.40065,
        'ns': 0,
        'pageid': 6422233,
        'primary': '',
        'title': 'Academy of Art University'}]}}
                
    class MockGetPlace:
        def __init__(self, url, params=None):
            pass
        def get_title(self):
            return IMITATION_RESPONSE_MEDIAWIKI_2['query']['geosearch'][0]['title']

    place =  MockGetPlace
    path = "models.mediawiki.MediaWiki.get_title"
    monkeypatch.setattr(path, place.get_title)

    assert place.get_title(IMITATION_RESPONSE_MEDIAWIKI_2) == 'Academy of Art University'


def test_get_extract_from_json_object_with_pageid(monkeypatch):

    IMITATION_RESPONSE_MEDIAWIKI_3 = {'batchcomplete': '',
                                'query': {'pages': {'6422233': {'canonicalurl': 'https://fr.wikipedia.org/wiki/Academy_of_Art_University',
                                'contentmodel': 'wikitext',
                                'editurl': 'https://fr.wikipedia.org/w/index.php?title=Academy_of_Art_University&action=edit',
                                'extract': 'L’Academy of Art University '
                                            '(autrefois Academy of Art '
                                            'College), est une université '
                                            'appartenant au Stephens '
                                            'Institute, fondée à San Francisco '
                                            'en Californie en 1929 par le '
                                            'peintre Richard S. Stephens.'}}}}
                
    class MockGetSummary:
        def __init__(self, url, params=None):
            pass
        def get_summary(self):
            page = 6422233
            return IMITATION_RESPONSE_MEDIAWIKI_3["query"]["pages"][str(page)]["extract"]

    summary =  MockGetSummary
    path = "models.mediawiki.MediaWiki.extract_summary"
    monkeypatch.setattr(path, summary.get_summary)

    assert summary.get_summary(IMITATION_RESPONSE_MEDIAWIKI_3) == "L’Academy of Art University (autrefois Academy of Art College), est une université appartenant au Stephens Institute, fondée à San Francisco en Californie en 1929 par le peintre Richard S. Stephens."




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
