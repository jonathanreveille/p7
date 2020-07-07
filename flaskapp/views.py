from flask import render_template, jsonify, request
from . import app

from .utils import transform_to_upper, find_position_of_place

# Créer la route de base
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Home")

# Créer l'onglet about
@app.route("/about")
def about():
    return render_template("about.html", title="About")


# @app.route("/ajax", methods=["POST"])
# def ajax():
    """Récupérer les données du navigateur par l'utilisateur"""
    # pour décoder la byteString et la rendre lisible et traitable en python on .decode()
    # user_text = request.data.decode() # <--becomes a STRING with .decode()
    # response = transform_to_upper(user_text)
    # print(response) # <--DICT
    # return jsonify(response)

    # c'est un dic

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.data.decode()
    response = find_position_of_place(user_text)
    return jsonify(response)


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

