#! /usr/bin/env python3
# coding : utf-8

import requests
import pprint as go

class MediaWiki:
    """class that will interact with MediaWiki API 
    with requests"""

    def __init__(self, latitude, longitude):

        self.search_json = dict()
        self.pageid = int()
        self.title = str()
        self.params_extract = dict()

        self.url = "https://fr.wikipedia.org/w/api.php"

        latitude = 37.786971 #to_test_1
        longitude = -122.399677 #to_test_2

        self.params = {
            "format":"json", #format de la réponse
            "action":"query", #action à réaliser
            "list": "geosearch", #méthode de recherche
            "gsradius":10000, #rayon de recherche autour des coordonnées GPS (max:10,000 m )
            "gscoord": f"{latitude}|{longitude}" #coordonnées GPS séparées par un pipe
        }

    def get_json(self):
        """Method to get json output from MediaWiki
        API."""

        self.search_req = requests.get(self.url, params = self.params)
        self.search_json = self.search_req.json()
        return self.search_json #this is a dictionary #go.pprint(self.search_json) #PrettyPrint method

    def get_title(self):
        """method to show the title f"om the
        geosearch coordinates"""
        self.title = self.search_json['query']['geosearch'][0]['title']
        return self.title
        #print("DEBUG1:", type(self.title))

    def get_page_id(self):
        """method to get the pageid, we need this information
        to extract data from MediaWiki"""
        self.page_id = self.search_json['query']['geosearch'][0]['pageid']
        return self.page_id
        #print("DEBUG2:", type(self.page_id))

    def get_short_description_from_pageid(self):
        """Method to extract short description
        from the pageid"""

        page_id = self.page_id

        self.params_extract = {
            "format": "json", # format de la réponse
            "action": "query", # action à effectuer
            "prop": "extracts|info", # Choix des propriétés pour les pages requises
            "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
            "exchars": 1200, # Nombre de caractères à retourner
            "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
            "pageids": page_id
            }
        #This returns us a value of 200 if it works, meaning, our code is connected to the API of MediaWiki with this query

        self.extract_response = requests.get(self.url, params=self.params_extract)

        if self.extract_response.status_code != 200:
            print("Query did not work, error status code")
        else:
            self.extracted_data = self.extract_response.json() #give us in ouput json object details
            go.pprint(self.extracted_data)

            return self.extracted_data

    def extract_summary(self):
        """method that get the summary from 
        the pageid json response"""

        page = self.page_id
        self.summary = self.extracted_data["query"]["pages"][str(page)]["extract"]
        
        return self.summary

def main():
    latitude = 37.78785
    longitude = -122.40065
    m = MediaWiki(latitude,longitude)
    m.get_json()
    m.get_title()
    m.get_page_id()
    m.get_short_description_from_pageid()
    m.extract_summary()


if __name__ == "__main__":
    main()



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