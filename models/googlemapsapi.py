#! /usr/bin/env python3
# coding : utf-8
import os
import requests
from models.location import Location
from dotenv import load_dotenv


# loading environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


class GoogleMaps:
    """Class for Google Maps services"""

    def __init__(self, query):

        self.search_url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
            "address": query,
            "key": SECRET_KEY
        }
        self.search_json = dict()
        self.location = dict()
        self.latitude = float()
        self.longitude = float()
        self.coords = list()

############################################
######## METHODS AFTER REFACTORING #########
############################################

    def receive_json(self): # REFACTORING
        """Returns coordinates json dict
        from the requests of address"""

        try:
            self.search_req = requests.get(self.search_url, params=self.params)
            # quand on recoit autre que status 200, ça génére une exception HTTPError
            return self.search_req.raise_for_status()

        except requests.exceptions.RequestException:
            self.search_json = {}
            return self.search_json
        
    def search_geocode(self): # REFACTORING
        """A method to retrieve only the information 
        we need from json"""

        self.search_json = self.search_req.json()
        self.location = self.search_json["results"][0]["geometry"]["location"]
        
        return self.location # get in output lat & lng from json, type dict.


    def find_positions(self):
        """method that creates lat, lng coordinates for use
        with Mediawiki"""

        lat = list()
        lng = list()
        lat.append(self.location.get("lat")) # output a list
        lng.append(self.location.get("lng")) # output a list

        self.latitude = lat[0]
        self.longitude = lng[0]
        self.coords.append(self.latitude) 
        self.coords.append(self.longitude)

        return self.latitude, self.longitude, self.coords

    def start_engine_google_maps(self):
        """method that launches the module
        when it's activated"""

        running = True

        if running:
            self.receive_json()
            self.search_geocode()
            self.find_positions()


############################################
####### METHODS BEFORE REFACTORING #########
############################################

    def get_json_test(self): #ORIGINAL

        self.search_req = requests.get(self.search_url, params=self.params)
        connexion = True

        if not connexion: #Fail
            print(
                self.search_req,
                "/--<Failed to connect to Google Maps WebService API>")

        else: #Success
            self.search_json = self.search_req.json()
            return self.search_json  # this is a dict


    def get_geocode_test(self): # ORIGINAL
        """A method to retrieve only the information 
        we need from json"""

        if not self.search_json:
            return None

        self.location = self.search_json["results"][0]["geometry"]["location"]
        return self.location
        # get in output lat & lng from json, type dict.


    def get_latitude_test(self): # ORIGINAL
        """Method to gather the longitude of the position
        we are seeking for"""

        if not self.search_json:
            return None

        self.longitude.append(self.location.get("lat"))
        return self.latitude[0]
        

    def get_longitude_test(self): # ORIGINAL
        """Method to gather the longitude of the position
        we are seeking for"""

        if not self.search_json:
            return None

        self.longitude.append(self.location.get("lng"))
        return self.longitude[0]



def main():
    # FOR USE, IT'S THE FOLLOWING ORDER
    g = GoogleMaps("Le musée d'Art Moderne de Paris")
    g.start_engine_google_maps()
    # pass


if __name__ == "__main__":
    main()


    # def find_positions(self):
    #     """Method to isolate latitude"""

    #     if not self.search_json:
    #         return None

    #     else:
    #         self.latitude.append(self.location.get("lat"))
    #         self.longitude.append(self.location.get("lng"))
    #         return self.latitude[0], self.longitude[0]


    # def get_clean_position(self):
    #     """Method to get the position in numbers lat and lng"""

    #     geopoint = Location(self.latitude[0], self.longitude[0])
    #     self.geopoint = geopoint
    #     print(self.geopoint)
    #     return self.geopoint




    # Penser à l'utilisateur qui instanciera la classe
    # et qui choisira d'entrer une adressse et d'avoir
    # en retour les points de géolocation directement
    # éviter tout les appels comme dans le main actuel
    # penser à l'ergonomie du programme


##########################################################################
##########################################################################
##########################################################################


# print("DEBUG3:", self.location["lat"])
    # print("DEBUG4:", self.location["lng"])
    # print("DEBUG5:", self.location.get("lat"))
    # print("DEBUG6:", self.location.get("lng"))
    # for coordinate in self.location:
    #     self.coordinates.append(self.location["lat"])
    #     self.coordinates.append(self.location["lng"])

    # print(self.coordinates)

# IT WORKS
    # self.coordinates = []

    # self.location = self.search_json["results"][0]["geometry"]["location"]
    # #^get lat & lng from json

    # self.coordinates.append(self.location) #add dict key:value to new list

    # print(self.coordinates)
    # print(len(self.coordinates))

    # self.location = self.search_json["results"][0]["geometry"]["location"]
    # print(self.location)
    # return self.location

##########################################################################
##########################################################################
##########################################################################
