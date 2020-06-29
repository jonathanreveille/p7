#! /usr/bin/env python3
# coding : utf-8

from models.parser import Parser
import pytest

def test_create_parser():
    p = Parser("")
    assert p.sentence == ""

# the keeper one
def test_capture_regular_expression():
    sentence = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    p = Parser(sentence)
    assert p.capture_regular_expression(sentence) == "où se trouve le musée d'art et d'histoire de Fribourg"


# #test2 - take important words 
# def test_remove_stop_words():
#     sentence = "salut grandpy a quel endroit se trouve le musee du louvre"
#     p = Parser(sentence)
#     assert p.remove_stop_words(sentence) == "musee louvre"


# def test_get_lower_cases():
#     p = Parser("Hello")
#     assert p.get_lower_cases() == "hello"

# def test_remove_spaces():
#     p = Parser("  Hello  ")
#     assert p.remove_spaces("  Hello l'o  ") == "Hello lo"

# def test_remove_all_accents():
#     p = Parser("éèêëãàäâåîïìöôòõñûüÿ")
#     assert p.remove_all_accents("éèêëãàäâåîïìöôòõñûüÿ") ==  "eeeeaaaaaiiioooonuuy"

# def test_take_away_special_characters():
#     p = Parser("Hello my name is Jon ,?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²")
#     assert p.remove_all_special_characters("hello my name is Jon ,?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²") \
#     == "Hello my name is Jon                                 "

# #test1 - take important words 
# def test_remove_stop_words():
#     sentence = "salut grandpy je souhaite savoir ou se situe la tour montparnasse"
#     p = Parser(sentence)
#     assert p.remove_stop_words(sentence) == "tour montparnasse"
