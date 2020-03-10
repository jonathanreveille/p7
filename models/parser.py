#! /usr/bin/env python3
# coding : utf-8

import unidecode


class Parser:
    
    def __init__(self, sentence):
        self.sentence = sentence

    def get_lower_cases(self):
        return self.sentence.lower()

    def remove_spaces(self, sentence):
        self.sentence = sentence
        no_space = self.sentence.strip()
        return no_space

    def remove_all_accents(self, sentence):
        # convert my string with unicode to remove accents
        unaccented_string = unidecode.unidecode(sentence)
        self.sentence = unaccented_string
        return self.sentence

    def remove_all_special_characters(self, sentence):
        sentence = ",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²"
        remove_spec_characters = "                                "
        delete = str.maketrans(sentence, remove_spec_characters)
        self.sentence = self.sentence.translate(delete)
        return self.sentence


def main():
    pass
    # parser = Parser("hello")
    # print(parser.sentence)

if __name__ == "__main__":
    main()


        

