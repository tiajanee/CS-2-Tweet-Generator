
import re
import random
 
 
def histogram(word_list):
    search = re.compile('\w+')
    histogram = {}  
 
    for word in word_list:
        if search.match(word) is None:
            continue

        if word not in histogram:
            histogram.update({word: 0})
 
        histogram[word] += 1
 
    return histogram
 
 
def unique_words(histogram):
     return len(histogram.keys())
 
 
def frequency(word, histogram):
    if word not in histogram:
         return 0
    
    return histogram[word]

def random_word():

    #rand_index = random.randrange(0, len(text_word_list))  
    #rand_word = text_word_list[rand_index]       

    rand_word =  random.choice(text_word_list)
    return rand_word
 
 
if __name__ == "__main__":
    text_file = open('practice_text.txt')
    text_word_list = [word.lower() for word in text_file.read().rsplit()]
    text_histogram = histogram(text_word_list)

    #rand_hist_word = random.choice(text_word_list)

    rand_word = random_word()

    print('Histogram:\t', text_histogram, '\n\n')
    print('Num of Unique_Words:\t', unique_words(text_histogram), '\n')
    print('"and" occurs:\t', frequency('and', text_histogram), 'times \n')
    print('"also" occurs:\t', frequency('also', text_histogram), 'times \n')
    print('"he" occurs:\t', frequency('he', text_histogram), 'times \n')
    print("A random word from this histogram is", rand_word)
    print("Another random word from this histogram is", rand_word)