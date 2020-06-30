from flask import render_template, jsonify, request, url_for
from . import app

from .utils import transform_to_upper


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/ajax", methods=["POST"])
def ajax():
    """récupérer les données du navigateur
    par l'utilisateur"""

    user_text = request.data.decode() #pour décoder la byteString et la rendre lisible et traitable en python
    response = transform_to_upper(user_text)
    return jsonify(response)


