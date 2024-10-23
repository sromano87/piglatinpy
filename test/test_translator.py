from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        # Arrange
        translator = PigLatinTranslator("hello world")
        # Act
        phrase = translator.get_phrase()
        # Assert
        self.assertEqual("hello world", phrase)
