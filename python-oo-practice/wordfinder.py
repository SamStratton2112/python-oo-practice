"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ''' Creates a list with several words as the elements and prints out
    the number of elements(words) in the list

    Conatains a method 'random' which returns a random word from the list'''


    def __init__(self, path):
        ''' sets up path to file with all words and returns number of words'''
        words_list = open(path)
        self.words = self.create_list(words_list)
        print(f'{len(self.words)} words read')
    
    
    def create_list(self, words_list):
        '''creates list of words withoug white space and \ n'''
        return [w.strip() for w in words_list]

    
    def random(self):
        '''returns a random word'''
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def create_list(self, words_list):
        """new list of words skipping blanks and comments."""

        return [w.strip() for w in words_list if w.strip() and not w.startswith("#")]

    
    

