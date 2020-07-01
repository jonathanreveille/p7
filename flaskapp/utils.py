# Nous utiliserons ce fichier pour traiter les
# donnés que nous allons récupérer avec le navigateur
# grâce à JS et ses méthodes.

def transform_to_upper(text):
    """ une méthode test pour vérifier qu'on
    agit bien sur la string reçu de l'utilisateur
    et on la renvoie en majuscule"""

    print(text)
    return {
        "text-original": text,
        "text-transformed": text.upper()
    }


# 1 créer une méthode pour récupérer le texte de l'user
# 2 Isoler la phrase texte sur laquelle nous allons travailler dessus
# 3 utiliser la méthode de Parser (class) pour regex
# 4 envoyer à Google Maps et récupérer Longitude latitude
# 5 Envoyer à media Wiki pour récupérer le résumé sur le lieu dit
# 6 retourner la réponse en f'string' pour que ce soit comme on veut
# 7 trouver la façon de pouvoir le réinjecter dans le HTML
