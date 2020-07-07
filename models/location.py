#! /usr/bin/env python3
# coding : utf-8

""" Class to create positions with latitude and longitude"""


class Location:

    def __init__(self, lat, lng):
        self.latitude = float(lat)
        self.longitude = float(lng)

    def __repr__(self):
        """Method that shows a string of the latitude
        and the longitude from the location we are looking
        for"""
        return f"Location : {self.latitude}, {self.longitude}"


if __name__ == "__main__":
    pass


def main():
    pass
