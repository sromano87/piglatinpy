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

    def test_translate_phrase_starting_with_vowel_o_ending_with_consonant(self):
        translator = PigLatinTranslator("ok")
        translation = translator.translate()
        self.assertEqual("okay", translation)

    def test_translate_phrase_starting_with_vowel_a_ending_with_consonant(self):
        translator = PigLatinTranslator("and")
        translation = translator.translate()
        self.assertEqual("anday", translation)

    def test_translate_phrase_starting_with_consonant_h(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)

    def test_translate_phrase_starting_with_consonant_c(self):
        translator = PigLatinTranslator("come")
        translation = translator.translate()
        self.assertEqual("omecay", translation)

    def test_translate_phrase_starting_with_two_consonants(self):
        translator = PigLatinTranslator("known")
        translation = translator.translate()
        self.assertEqual("ownknay", translation)

    def test_translate_phrase_starting_with_more_than_two_consonants(self):
        translator = PigLatinTranslator("spring")
        translation = translator.translate()
        self.assertEqual("ingspray", translation)

    def test_translate_phrase_with_only_consonants(self):
        translator = PigLatinTranslator("fly")
        translation = translator.translate()
        self.assertEqual("flyay", translation)

    def test_translate_phrase_with_more_words(self):
        translator = PigLatinTranslator("hello world")
        translation = translator.translate()
        self.assertEqual("ellohay orldway", translation)

    def test_translate_phrase_with_composite_words(self):
        translator = PigLatinTranslator("well-being")
        translation = translator.translate()
        self.assertEqual("ellway-eingbay", translation)

    def test_translate_phrase_with_more_and_composite_words(self):
        translator = PigLatinTranslator("hello well-being")
        translation = translator.translate()
        self.assertEqual("ellohay ellway-eingbay", translation)

    def test_translate_phrase_with_exclamation_mark(self):
        translator = PigLatinTranslator("hello world!")
        translation = translator.translate()
        self.assertEqual("ellohay orldway!", translation)