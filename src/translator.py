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
        first_char = self._phrase[0]
        if first_char in VOWELS:
            return self._translate_word_starting_vowel()
        elif first_char in CONSONANTS:
            return self._translate_word_starting_consonant()
        else:
            raise PigLatinError

    def _translate_word_starting_vowel(self) -> str:
        last_char = self._phrase[-1]
        if last_char == "y":
            return self._phrase + "nay"
        if last_char in VOWELS:
            return self._phrase + "yay"
        if last_char in CONSONANTS:
            return self._phrase + "ay"
        else:
            raise PigLatinError

    def _translate_word_starting_consonant(self) -> str:
        suffix = ""
        for char in self._phrase:
            if char in CONSONANTS:
                suffix += char
            else:
                break
        return self._phrase[len(suffix):] + suffix + "ay"