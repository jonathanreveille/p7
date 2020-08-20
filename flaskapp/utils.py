# Nous utiliserons ce fichier pour traiter les
# donnés que nous allons récupérer avec le navigateur
# grâce à JS et ses méthodes.

from models.parser import Parser
from models.googlemapsapi import GoogleMaps
from models.mediawiki import MediaWiki
from config.constant import positive_answers, negative_answers
from random import *


def find_place_in_sentence(text):
    """ Returns the position of the place the usertext
    is looking for """
    parser = Parser(text)
    parser.capture_regular_expression(text)
    address_ask_by_user = parser.address
    return address_ask_by_user

def find_geocoords_with_google_maps(location):
    """ Method that will use GM to find 
    coordinates of the position """
    
    gm = GoogleMaps(location)
    gm.start_engine_google_maps(start="True")

    mw = MediaWiki(gm.latitude, gm.longitude)
    mw.start_engine_mediawiki()

    summary = mw.summary
    url = mw.fullurl
    latitude = mw.latitude
    longitude = mw.longitude

    return summary, url, latitude, longitude


def generate_positive_answer():
    """this method will take randomly 
    a positive answer for Grandpy's reply"""

    positive_answer = choice(positive_answers)
    return positive_answer
    

def generate_negative_answer():
    """this method will take randomly 
    a negative answer for Grandpy's reply"""
    
    negative_answer = choice(negative_answers)
    return negative_answer


if __name__ == "__main__":
    generate_positive_answer()
    generate_negative_answer()

# def find_coords(location):

#     gm = GoogleMaps(location)
#     gm.start_engine_google_maps()

#     latitude = gm.latitude
#     longitude = gm.longitude

#     return latitude, longitude

# def find_summary(**kwargs):

#     mw = MediaWiki(latitude, longitude)
#     mw.start_engine_mediawiki()

#     summary = mw.summary
#     url = mw.url

#     return summary, url

# 1 créer une méthode pour récupérer le texte de l'user
# 2 Isoler la phrase texte sur laquelle nous allons travailler dessus
# 3 utiliser la méthode de Parser (class) pour regex
# 4 envoyer à Google Maps et récupérer Longitude latitude
# 5 Envoyer à media Wiki pour récupérer le résumé sur le lieu dit
# 6 retourner la réponse en f'string' pour que ce soit comme on veut
# 7 trouver la façon de pouvoir le réinjecter dans le HTML



# def transform_to_upper(text):
#     """ Une méthode test pour vérifier qu'on
#     agit bien sur la string reçu de l'utilisateur
#     et on la renvoie en majuscule"""

#     print(text)
#     return {
#         "text-original": text,
#         "text-transformed": text.upper()
#     }
