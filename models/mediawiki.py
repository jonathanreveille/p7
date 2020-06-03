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
        #go.pprint(self.search_json) #PrettyPrint method
        return self.search_json #this is a dictionary

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

    def extract_short_description(self):
        """Method to extract short description
        from the pageid"""
        pass

def main():
    latitude = 37.78785
    longitude = -122.40065
    m = MediaWiki(latitude,longitude)
    m.get_json()
    m.get_title()
    m.get_page_id()
    m.get_extract_short_description()



if __name__ == "__main__":
    main()

