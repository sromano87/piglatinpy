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

