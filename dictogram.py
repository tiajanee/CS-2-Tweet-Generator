from __future__ import division, print_function  # Python 2 and 3 compatibility
import re

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
                self.types += 1

    def add_count(self, word, word_list, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        #search = re.compile('\w+')  
        for word in word_list:
            if self.add_count(word) is None:
                continue

            if self.types == 0:
                self.add_count(word)
                self.types += 1
 
        histogram[word] += 1
        self.tokens += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word not in histogram:
         return 0
    
        return self.word



def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()



def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())

    text_file = open('fish.txt')
    #splits words in file into lines and make the all lower case for the unique_words() function
    text_word_list = [word.lower() for word in text_file.read().rsplit()]
    #saves histogram in a variable
    text_histogram = histogram(text_word_list)
    print(text_histogram)


if __name__ == '__main__':
    main()
