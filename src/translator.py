from gettext import translation

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
        self.phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"
        word = ""
        translation = ""
        for i,char in enumerate(self.phrase):
            if char == " " or char == "-" or char == "!":
                translation += PigLatinTranslator.translate_word(word) + char
                word = ""
            elif i == len(self.phrase) - 1:
                word += char
                translation += PigLatinTranslator.translate_word(word)
            else:
                word += char
        return translation


    @staticmethod
    def translate_word(word: str) -> str:
        first_letter = word[0]
        if first_letter in VOWELS:
            return PigLatinTranslator.translate_word_starting_with_vowel(word)
        elif first_letter in CONSONANTS:
            return PigLatinTranslator.translate_word_starting_with_consonant(word)


    @staticmethod
    def translate_word_starting_with_consonant(word):
        n_consonants = 0
        for letter in word:
            if letter in CONSONANTS:
                n_consonants += 1
            else:
                break
        starting_consonants = word[:n_consonants]
        substring = word[n_consonants:]
        return substring + starting_consonants + "ay"

    @staticmethod
    def translate_word_starting_with_vowel(word):
        last_letter = word[-1]
        if last_letter == "y":
            return word + "nay"
        elif last_letter in VOWELS:
            return word + "yay"
        else:
            return word + "ay"
