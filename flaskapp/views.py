from flask import render_template, jsonify, request
from . import app

from .utils import transform_to_upper

# Créer la route de base


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Home")

# Créer l'onglet about


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/ajax", methods=["POST"])
def ajax():
    """Récupérer les données du navigateur
    par l'utilisateur"""

    # pour décoder la byteString et la rendre lisible et traitable en python
    user_text = request.data.decode()
    response = transform_to_upper(user_text)
    return jsonify(response)  # c'est un dic


# ^^^EXPLICATIONS^^^
# créer des routes pour notre application
# on peut paramètrer un title afin  qu'il s'affiche
# lorsqu'on est sur cette page
# render_template permet de chercher dans le directory
#  le bon fichier seul
# app.route("/nomdelapage") --> il s'affichera
# localhost:5000/about p
# ar exemple pour la page about
