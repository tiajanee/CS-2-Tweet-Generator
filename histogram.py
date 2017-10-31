
import re
 
 
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
 
 
if __name__ == "__main__":
    text_file = open('practice_text.txt')
    text_word_list = [word.lower() for word in text_file.read().rsplit()]
    text_histogram = histogram(text_word_list)
    print('Histogram:\t', text_histogram, '\n\n')
    print('Num of Unique_Words:\t', unique_words(text_histogram), '\n')
    print('"but" occurs:\t', frequency('but', text_histogram), 'times \n')