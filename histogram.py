
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

def random_word(histogram):       

    rand_word =  random.choice(list(histogram.keys()))
    return rand_word

# def weighted_freq(histogram, word_list):
    
#     word_weight = histogram.keys() / (sum(word_list))
#     rand_int = random.randrange(0,1)
#     for word in histogram:
#         if word_weight < rand_int:
#             continue
#         if word_weight > rand_int:
#             print(word)
 
if __name__ == "__main__":
    text_file = open('practice_text.txt')
    text_word_list = [word.lower() for word in text_file.read().rsplit()]
    text_histogram = histogram(text_word_list)

    print('Histogram:\t', text_histogram, '\n\n')
    print('Num of Unique_Words:\t', unique_words(text_histogram), '\n')
    print('"and" occurs:\t', frequency('and', text_histogram), 'times \n')
    print('"red" occurs:\t', frequency('red', text_histogram), 'times \n')
    print('"he" occurs:\t', frequency('he', text_histogram), 'times \n')
    print("A random word from this histogram is", random_word(text_histogram))
    print("Another random word from this histogram is", random_word(text_histogram))
    #print("This is a weighted random word", weighted_freq(text_histogram, text_word_list))