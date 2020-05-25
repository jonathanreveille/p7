#! /usr/bin/env python3
# coding : utf-8

import re

chaine1 = "Salut Grandpy, je souhaiterai savoir ou se situe le Musée du Louvre"
chaine2 = "Salut Grandpy, j'espère que tu vas bien ? Pourrais-tu me dire l'adresse du Musée de la Marionnette"
chaine3 = "Salut Grandpy, tout roule de ton côté ? Mamie va bien? Je me disais l'autre jour, si tu pouvais me dire a quel endroit est la Tour Montparnasse"
chaine4 = "Hey Grandpy, tout va bien mon ancien ? Peux-tu me dire ou se trouve l'emplacement de la Chaise Verte?"
chaine5 = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
chaine6 = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."

regex = r"(l'adresse (de|du)|ou est|ou se situe|ou se trouve|a quel endroit est|indiquer) ([^,.:;!?]+)"

match1 = re.search(regex, chaine1)
print("match  1: ", match1)

match2 = re.search(regex, chaine2)
print("match  2: ", match2)

match3 = re.search(regex, chaine3)
print("match  3: ", match3)

adresse1 = match1.group(3)
print(adresse1)

adresse2 = match2.group(3)
print(adresse2)

adresse3 = match3.group(3)
print(adresse3)

match4 = re.search(regex, chaine4)
print(" match 4 : ", match4)
adresse4 = match4.group(3)
print(adresse4)

match5 = re.search(regex, chaine5)
print(" match 5 : ", match5)
adresse5 = match5.group(3)
print(adresse5)

match6 = re.search(regex, chaine6)
print(" match 6 : ", match6)
adresse6 = match6.group(3)
print(adresse6)

#Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?".
#Une autre: "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.
