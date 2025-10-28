from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello word")
        phrase = translator.get_phrase()
        self.assertEqual("hello word", phrase)

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_phrase_starting_with_vowel_a_ending_with_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_translate_phrase_starting_with_vowel_e_ending_with_y(self):
        translator = PigLatinTranslator("enemy")
        translation = translator.translate()
        self.assertEqual("enemynay", translation)

    def test_translate_phrase_starting_with_vowel_u_ending_with_vowel_a(self):
        translator = PigLatinTranslator("umbrealla")
        translation = translator.translate()
        self.assertEqual("umbreallayay", translation)

    def test_translate_phrase_starting_with_vowel_i_ending_with_vowel_e(self):
        translator = PigLatinTranslator("induce")
        translation = translator.translate()
        self.assertEqual("induceyay", translation)