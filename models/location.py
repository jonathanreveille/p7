#! /usr/bin/env python3
# coding : utf-8

""" Class to create positions with latitude and longitude"""


class Location:

    def __init__(self, lat, lng):
        self.latitude = float(lat)
        self.longitude = float(lng)

    def __repr__(self):
        """Method that presents in first position
        latitude, and second position the longitude of
        a place """

        return f"Location : {self.latitude}, {self.longitude}"


if __name__ == "__main__":
    pass


def main():
    pass
