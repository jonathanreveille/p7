#! /usr/bin/env python3
# coding : utf-8
import os
import requests
from models.location import Location
from dotenv import load_dotenv


#loading environment variables
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

    def get_json(self):
        """Returns coordinates json dict
        from the requests of address"""

        self.search_req = requests.get(self.search_url, params=self.params)
        connexion = True

        if not connexion:
            print(self.search_req, "/--<Failed to connect to Google Maps WebService API>")
        else:
            print(self.search_req,">--<Connected to Google Maps Webservice API Suceed>")
            self.search_json = self.search_req.json()

        return self.search_json #this is a dict

    def get_geocode(self):
        """method to get only the information we need from json"""

        self.coordinates = []
        self.location = self.search_json["results"][0]["geometry"]["location"]
        return self.location
        #get in output lat & lng from json, type dict.

    def get_latitude(self):
        """Method to isolate latitude"""

        self.latitude = list()
        self.latitude.append(self.location.get("lat"))
        return self.latitude


    def get_longitude(self):
        """Method to isolate longitude"""

        self.longitude = []
        self.longitude.append(self.location.get("lng"))
        return self.longitude[0]

    def get_clean_position(self):
        """Method to get positions numbers lat and lng"""

        self.geopoint = Location(self.latitude[0], self.longitude[0])
        return self.geopoint
 

def main():
    g = GoogleMaps("Musée du Louvre, Paris")
    g.get_json()
    g.get_geocode()
    g.get_latitude()
    g.get_longitude()
    g.get_clean_position()

if __name__ == "__main__":
    main()


###############################################################################################
###############################################################################################
###############################################################################################


# print("DEBUG3:", self.location["lat"])
        # print("DEBUG4:", self.location["lng"])
        # print("DEBUG5:", self.location.get("lat"))
        # print("DEBUG6:", self.location.get("lng"))
        # for coordinate in self.location:
        #     self.coordinates.append(self.location["lat"])
        #     self.coordinates.append(self.location["lng"])
        
        # print(self.coordinates)
        
#IT WORKS
        # self.coordinates = []

        # self.location = self.search_json["results"][0]["geometry"]["location"] 
        # #^get lat & lng from json

        # self.coordinates.append(self.location) #add dict key:value to new list

        # print(self.coordinates)
        # print(len(self.coordinates))

        # self.location = self.search_json["results"][0]["geometry"]["location"]
        # print(self.location)
        # return self.location

###############################################################################################
###############################################################################################
###############################################################################################
