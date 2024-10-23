from src.error import PigLatinError

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self._phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self._phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self._phrase == "":
            return "nil"
        return PigLatinTranslator._translate_word(self._phrase)


    @staticmethod
    def _translate_word(word: str) -> str:
        first_char = word[0]
        if first_char in VOWELS:
            return PigLatinTranslator._translate_word_starting_vowel(word)
        elif first_char in CONSONANTS:
            return PigLatinTranslator._translate_word_starting_consonant(word)
        else:
            raise PigLatinError

    @staticmethod
    def _translate_word_starting_vowel(word) -> str:
        last_char = word[-1]
        if last_char == "y":
            return word + "nay"
        if last_char in VOWELS:
            return word + "yay"
        if last_char in CONSONANTS:
            return word + "ay"
        else:
            raise PigLatinError

    @staticmethod
    def _translate_word_starting_consonant(word) -> str:
        suffix = ""
        for char in word:
            if char in CONSONANTS:
                suffix += char
            else:
                break
        return word[len(suffix):] + suffix + "ay"