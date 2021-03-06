#! /usr/bin/env python3
# coding : utf-8

import requests
import pprint as go
from models.googlemapsapi import GoogleMaps


class MediaWiki:
    """class that will interact with MediaWiki API
    with requests"""

    def __init__(self, latitude, longitude):
        
        ###ORIGINAL###
        # self.googlemaps = GoogleMaps
        # self.positions = self.googlemaps.coords

        # for position in self.positions:
        #     self.latitude = self.positions[0]
        #     self.longitude = self.positions[1]

        self.latitude = latitude
        self.longitude = longitude

        self.search_json = dict()
        self.pageid = int()
        self.title = str()
        self.fullurl = str()
        self.summary = str()
        self.params_extract = dict()
        self.url = "https://fr.wikipedia.org/w/api.php"

        self.params = {
            "format": "json",  # format de la réponse
            "action": "query",  # action à réaliser
            "list": "geosearch",  # méthode de recherche
            # rayon de recherche autour des coordonnées GPS (max:10,000 m )
            "gsradius": 10000,
            # coordonnées GPS séparées par un pipe
            "gscoord": f"{latitude}|{longitude}"
        }

    def get_json(self):
        """Method to get json output from MediaWiki
        API."""

        self.search_req = requests.get(self.url, params=self.params)
        self.search_json = self.search_req.json()
        # this is a dictionary #go.pprint(self.search_json) #PrettyPrint method
        return self.search_json

    def get_title(self):
        """method to show the title f"om the
        geosearch coordinates"""
        self.title = self.search_json['query']['geosearch'][0]['title']
        return self.title
        # print("DEBUG1:", type(self.title))

    def get_page_id(self):
        """method to get the pageid, we need this information
        to extract data from MediaWiki"""
        self.page_id = self.search_json['query']['geosearch'][0]['pageid']
        return self.page_id
        # print("DEBUG2:", type(self.page_id))

    def get_short_description_from_pageid(self):
        """Method to extract short description
        from the pageid"""

        page_id = self.page_id

        self.params_extract = {
            "format": "json",  # format de la réponse
            "action": "query",  # action à effectuer
            "prop": "extracts|info",  # Choix des propriétés pour les pages requises
            # Fournit une URL complète, une URL de modification, et l’URL
            # canonique de chaque page.
            "inprop": "url", #il faut que je récupère ça pour l'afficher sur mon siteweb
            "exchars": 1200,  # Nombre de caractères à retourner
            # Renvoyer du texte brut (éliminer les balises de markup)
            "explaintext": 1,
            "pageids": page_id
        }
        # This returns us a value of 200 if it works, meaning, our code is
        # connected to the API of MediaWiki with this query

        self.extract_response = requests.get(
            self.url, params=self.params_extract)

        if self.extract_response.status_code != 200:
            print("Query did not work, error status code")
        else:
            # give us in ouput json object details
            self.extracted_data = self.extract_response.json()
            #go.pprint(self.extracted_data)
            return self.extracted_data

    def extract_summary(self):
        """method that get the summary from
        the pageid json response"""

        page = self.page_id
        self.summary = self.extracted_data["query"]["pages"][str(
            page)]["extract"]
            
        print(self.summary[0:500])
        return self.summary

    def extract_fullurl(self):
        """method that takes the fullurl from
        mediawiki if the user wants to learn
        more information"""

        page = self.page_id
        self.fullurl = self.extracted_data["query"]["pages"][str(
            page)]["fullurl"]

        print("Pour plus d'information:", self.fullurl)
        return self.fullurl


    def start_engine_mediawiki(self):
        """method that is friendly user for use of 
        the application"""
        
        running = True
        
        if running:
            self.get_json()
            self.get_title()
            self.get_page_id()
            self.get_short_description_from_pageid()
            self.extract_summary()
            self.extract_fullurl()


def main():
    
    ## PARTIE AVEC LE PARSER 
    ## CREER PARSER, PRENDRE LA PHRASE, FAIRE USINE
    ## ACCEDER A L ATTRIBUT SENTENCE DE PARSER ET 
    ## INSERER DANS LE PARAMETRE DE GOOGLEMAPS CLASS
    g = GoogleMaps("Le musée d'Art Moderne de Paris")
    g.start_engine_google_maps()

    m = MediaWiki(g.latitude, g.longitude)
    m.start_engine_mediawiki()


if __name__ == "__main__":
    main()



    # Penser à l'utilisateur qui instanciera la classe
    # et qui choisira d'entrer une adressse et d'avoir
    # en retour les points de géolocation directement
    # éviter tout les appels comme dans le main actuel
    # penser à l'ergonomie du programme (GMaps et MWiki)




    ### REFACTORING THIS UNDER ###
    # m.get_json()
    # m.get_title()
    # m.get_page_id()
    # m.get_short_description_from_pageid()
    # m.extract_summary()
    # m.extract_fullurl()



# page_id = self.page_id
# self.summary = self.extracted_data["query"]["pages"][page_id][0]["extract"]
# print(self.summary)

# if self.extract_response.status_code == 200:
#     self.extracted_data = self.extract_response.json() #give us in ouput json object details
#     return self.extracted_data
#     #go.pprint(self.extracted_data)
#     #print((self.extracted_data["query"]["pages"]["6422233"]["extract"]))
# else:
#     print("Query did not work, error status code")
