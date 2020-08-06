from flask import render_template, jsonify, request
from . import app

from .utils import find_place_in_sentence, find_geocoords_with_google_maps, generate_positive_answer, generate_negative_answer

import os
from dotenv import load_dotenv
# loading environment variables
load_dotenv()
API_KEY_FRONT= os.getenv("SECRET_KEY_FRONT")


# Créer la route de base
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Home", API_KEY=API_KEY_FRONT )

# Créer l'onglet about
@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/ajax", methods=["POST"])
def ajax():

    data = {"status": False}

    user_text = request.data.decode()
    response = find_place_in_sentence(user_text)

    if not response:
        data = {"status": False,
                "question":user_text,
                "answer": generate_negative_answer(),
                }

    if response:
        all_text, url, latitude, longitude = find_geocoords_with_google_maps(response)
        data = {"status" : True,
                "location" : response,
                "article" : all_text,
                "answer": generate_positive_answer(),
                "url":url,
                "latitude" : latitude,
                "longitude" : longitude,
                }

    return jsonify(data)

    
    # data = {"status": False}

    # user_text = request.data.decode()
    # response = find_place_in_sentence(user_text)

    # if not response:
    #     data = {"status": False,
    #             "question":user_text,
    #             "answer": "Désolé, je n'ai pas trouvé"
    #             }

    # if response:
    #     all_text, url = find_geocoords_with_google_maps(response)
    #     data = {"status" : True,
    #             "location" : response,
    #             "article" : all_text,
    #             "answer": "C'est bon j'ai trouvé mon grand",
    #             "url":url
    #             }
    #     answer = data
    # return jsonify(data)


# NORMAL
# @app.route("/ajax", methods=["POST"])
# def ajax():
#     user_text = request.data.decode()
#     response = find_place_in_sentence(user_text)
#     print(response) # string
#     return jsonify(response)




# geocoords = find_geocoords_with_google_maps(response)
# summary = get_back_info_mediawiki()
# @app.route("/ajax", methods=["POST"])
# def ajax():
    """Récupérer les données du navigateur par l'utilisateur"""
    # pour décoder la byteString et la rendre lisible et traitable en python on .decode()
    # user_text = request.data.decode() # <--becomes a STRING with .decode()
    # response = transform_to_upper(user_text)
    # print(response) # <--DICT
    # return jsonify(response)

    # c'est un dic



# ^^^EXPLICATIONS^^^
# créer des routes pour notre application
# on peut paramètrer un title afin  qu'il s'affiche
# lorsqu'on est sur cette page
# render_template permet de chercher dans le directory
#  le bon fichier seul
# app.route("/nomdelapage") --> il s'affichera
# localhost:5000/about p
# ar exemple pour la page about


#Le terminal de FLASK est le serveur
# views.py est le fichier qui fait les routes de mon 
# application (les nouvelles pages)
# il me permet de récupérer des informations de mon navigateur web

# utils.py me permet de "traiter" l'information reçu par le 
# navigateur web.
# nous importons les méthodes de utils pour ensuite 
# RENVOYER avec views.py la réponse traitée par notre code

