# Nous utiliserons ce fichier pour traiter les
# donnés que nous allons récupérer avec le navigateur
# grâce à JS et ses méthodes.

from models.parser import Parser

def transform_to_upper(text):
    """ Une méthode test pour vérifier qu'on
    agit bien sur la string reçu de l'utilisateur
    et on la renvoie en majuscule"""

    print(text)
    return {
        "text-original": text,
        "text-transformed": text.upper()
    }

def find_position_of_place(text):
    """ Returns the position of the place the usertext
    is looking for"""
    parser = Parser(text)
    parser.capture_regular_expression(text)
    address_ask_by_user = parser.address
    return address_ask_by_user

def send_to_google_maps():
    print(address_ask_by_user)
    
# 1 créer une méthode pour récupérer le texte de l'user
# 2 Isoler la phrase texte sur laquelle nous allons travailler dessus
# 3 utiliser la méthode de Parser (class) pour regex
# 4 envoyer à Google Maps et récupérer Longitude latitude
# 5 Envoyer à media Wiki pour récupérer le résumé sur le lieu dit
# 6 retourner la réponse en f'string' pour que ce soit comme on veut
# 7 trouver la façon de pouvoir le réinjecter dans le HTML
