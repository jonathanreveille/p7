#! /usr/bin/env python3
# coding : utf-8

import unidecode
import re

class Parser:
    
    def __init__(self, sentence):
        self.sentence = sentence


    def capture_regular_expression(self, sentence): # One block that does everything almost
        """method that captures location in 
        string, regular expression"""

        sentence = str(sentence)

        regex = r"(l'adresse (de|du)|où est|où se situe|où se trouve|à quel endroit est|indiquer|me montrer) (?P<lieu>[^,.:;!?]+)"
        match = re.search(regex, sentence)
        address = match.group("lieu") #ou group(3)
        self.address = address

        return self.address

def main():
    pass

if __name__ == "__main__":
    pass

    # def get_lower_cases(self):
    #     """method to return sentence in lower cases"""
    #     return self.sentence.lower()

    # def remove_all_accents(self, sentence):
    #     """method to remove all accents with unidecode"""
    #     # convert my string with unicode to remove accents
    #     unaccented_string = unidecode.unidecode(sentence)
    #     self.sentence = unaccented_string
    #     return self.sentence

    # def remove_all_special_characters(self, sentence):
    #     """method to remove all special characters
    #     from the string 'sentence'"""
    #     remove_spec_characters = "                                "
    #     to_translate = str.maketrans(self.special_characters, remove_spec_characters)
    #     self.sentence = self.sentence.translate(to_translate)
    #     return self.sentence

    # def remove_spaces(self, sentence):
    #     """method to remove all spaces beggining and end,
    #     and removes repetitive spaces"""
    #     self.sentence = sentence.strip().replace("  ", " ").replace("   ", " ").replace("'", "")
    #     return self.sentence
    
    # def remove_stop_words(self, sentence):
    #     """method that removes all useless words in sentence,
    #     we get in return the main info from the sentence """
        
    #     cleaned_sentence = []

    #     for word in self.sentence.split(): # maybe add a new list
    #         if word in STOP_WORDS:
    #             pass
    #         if word not in STOP_WORDS:
    #             cleaned_sentence.append(word)
    #         if word == " ":
    #             pass
    #         self.cleaned_sentence = " ".join(cleaned_sentence)

    #     return self.cleaned_sentence



    # commencer par test
    # create a method using library re
    # create differents lists : introduction à une question pour un lieu
    # préparer des réponses positives
    # préparer des réponses négatives (reformuler la question du utilisateur)
    # préparer la variable qui retient seulement le lieu en question (group1,2,3 choisir groupe 3)



        

