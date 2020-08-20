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

    try:
        all_text, url, latitude, longitude = find_geocoords_with_google_maps(response)
        
        if latitude and longitude != None:
            data = {"status" : True,
                "location" : response,
                "article" : all_text,
                "answer": generate_positive_answer(),
                "url":url,
                "latitude" : latitude,
                "longitude" : longitude,
                "question": user_text,
                }
        else:
            data = {"status": False,
                    "question": user_text,
                    "answer": generate_negative_answer(),
                    }
                    
    except TypeError:
        raise(TypeError," DEBUG2: no georcoods found")   

    return jsonify(data)


##  ORIGINAL
# @app.route("/ajax", methods=["POST"])
# def ajax():

#     data = {"status": False}

#     user_text = request.data.decode()
#     response = find_place_in_sentence(user_text)

#     if response:
#         all_text, url, latitude, longitude = find_geocoords_with_google_maps(response) 
#         # ^ c'est ici où sa bug si on ne trouve pas de latitude et longitude
#         # la condition IF ne sert à rien à cet endroit
#         # car on rentre dedans, car parser trouvera toujours un lieu
#         # qui peut être bon ou pas bon
#         data = {"status" : True,
#                 "location" : response,
#                 "article" : all_text,
#                 "answer": generate_positive_answer(),
#                 "url":url,
#                 "latitude" : latitude,
#                 "longitude" : longitude,
#                 "question": user_text,
#                 }

#     elif not response:
#         data = {"status": False,
#                 "question":user_text,
#                 "answer": generate_negative_answer(),
#                 }

#     return jsonify(data)


# # retour REPONSE NEGATIVE MEME SI LOCATION EST BONNE
# @app.route("/ajax", methods=["POST"])
# dej ajax():

#     data = {"status": False}

#     user_text =  request.data.decode() # decode le binary string en string
#     response = find_place_in_sentence(user_text)

#     all_text, url, latitude, longitude = find_geocoords_with_google_maps(response)

#     if latitude or longitude == None:
#         data = {"status": False,
#         "question":user_text,
#         "answer": generate_negative_answer(),
#         }

#     elif latitude or longitude != None:
#         data = {"status" : True,
#                 "location" : response,
#                 "article" : all_text,
#                 "answer": generate_positive_answer(),
#                 "url":url,
#                 "latitude" : latitude,
#                 "longitude" : longitude,
#                 "question": user_text,
#                 }

#     return jsonify(data) 


# # NE FONCTIONNE PAS...
# @app.route("/ajax", methods=["POST"])
# def ajax():

#     data = {"status": False}

#     user_text =  request.data.decode() # decode le binary string en string
#     response = find_place_in_sentence(user_text)

#     coords = find_geocoords_with_google_maps(response)
#     print("DEBUg1", coords)

#     listcoord = []
    
#     for value in len(coords):
#         listcoord.append(value)

#         if len(listcoords) == 3:
#             data = {"status" : True,
#             "location" : response,
#             "article" : listcoord[0],
#             "answer": generate_positive_answer(),
#             "url":listcoord[1],
#             "latitude" : listcoord[2],
#             "longitude" : listcoord[3],
#             "question": user_text,
#             }

#         else:
#             data = {"status": False,
#             "question":user_text,
#             "answer": generate_negative_answer(),
#             }

#     return jsonify(data) 



# ##  RETOUR REPONSE POSITIVE, bug SUR REPONSE NEGATIVE
# ## INTERNAL ERROR SERVER ERROR 500
# ## script.js:86 Uncaught (in promise) TypeError: Cannot read property 'question' of undefined
# ## at script.js:86

# @app.route("/ajax", methods=["POST"])
# def ajax():

#     data = {"status": False}

#     user_text = request.data.decode()
#     response = find_place_in_sentence(user_text)

#     all_text, url, latitude, longitude = find_geocoords_with_google_maps(response)

#     dic_donnees = {
#                 "article": all_text,
#                 "url":url,
#                 "latitude":latitude,
#                 "longitude":longitude,
#                 }

#     found = False
    
#     if dic_donnees["latitude"] and dic_donnees["longitude"]:
#         found = True
#         data = {"status" : True,
#             "location" : response,
#             "article" : all_text,
#             "answer": generate_positive_answer(),
#             "url":url,
#             "latitude" : latitude,
#             "longitude" : longitude,
#             "question": user_text,
#             }

#     if not dic_donnees["latitude"] and not dic_donnees["longitude"]:
#         found = False
#         data = {"status": False,
#                 "question": user_text,
#                 "answer": generate_negative_answer(),
#                 }


#     return jsonify(data)




    # # all_text, url, latitude, longitude = find_geocoords_with_google_maps(response)

    # if latitude and longitude != None:

    # elif latitude and longitude == None:


# @app.route("/ajax", methods=["POST"])
# def ajax():

#     data = {"status": False}

#     user_text = request.data.decode()
#     response = find_place_in_sentence(user_text)

#     if response:
#         all_text, url, latitude, longitude = find_geocoords_with_google_maps(response) 
#         # ^ c'est ici où sa bug si on ne trouve pas de latitude et longitude
#         # la condition IF ne sert à rien à cet endroit
#         # car on rentre dedans, car parser trouvera toujours un lieu
#         # qui peut être bon ou pas bon
#         data = {"status" : True,
#                 "location" : response,
#                 "article" : all_text,
#                 "answer": generate_positive_answer(),
#                 "url":url,
#                 "latitude" : latitude,
#                 "longitude" : longitude,
#                 "question": user_text,
#                 }

#     elif not response:
#         data = {"status": False,
#                 "question":user_text,
#                 "answer": generate_negative_answer(),
#                 }

#     return jsonify(data)

    
    # ORINALE QUI FONCTIONNE LORSQUE LES GEO COORDS SONT TROUVEES
# @app.route("/ajax", methods=["POST"])
# def ajax():
    # data = {"status": False}

    # user_text = request.data.decode()
    # response = find_place_in_sentence(user_text)

    # if response:
    #     all_text, url, latitude, longitude = find_geocoords_with_google_maps(response) 
    #     # ^ c'est ici où sa bug si on ne trouve pas de latitude et longitude
    #     # la condition IF ne sert à rien à cet endroit
    #     # car on rentre dedans, car parser trouvera toujours un lieu
    #     # qui peut être bon ou pas bon
    #     data = {"status" : True,
    #             "location" : response,
    #             "article" : all_text,
    #             "answer": generate_positive_answer(),
    #             "url":url,
    #             "latitude" : latitude,
    #             "longitude" : longitude,
    #             "question": user_text,
    #             }

    # elif not response:
    #     data = {"status": False,
    #             "question":user_text,
    #             "answer": generate_negative_answer(),
    #             }

    # return jsonify(data)


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

