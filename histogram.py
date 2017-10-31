import re

def histogram(word_list):
	
	histogram = {}
	search = re.compile('\w+')

	for word in word_list:
		if search.match(word) is None:
			pass

			if word not in histogram:
				histogram.update({word: 0})


			histogram[word] += 1

		return histogram



def unique_words(histogram):
	variety = len(histogram.keys())
	return variety


def frequency(word, histogram):

	 if word not in histogram:
	 	return 0

	 return histogram[word]

