"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class that finds random words from a specific dictionary."""

    def __init__(self, path):
        """This will read the dictionary and print the # of items read."""

        word_file = open(path)
        self.words = self.parse(word_file)
        print(f"{len(self.words)} words read")

    def parse(self, word_file):
        """Read through the list of words in "word_file". """
        return [w.strip() for w in word_file
                if w.strip() and not w.startswith("#")]
       
    def random(self):
        """Returns a random word."""
        return random.choice(self.words)
    

