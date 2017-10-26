import random
import sys

'''

Takes file of words from local directory and puts them in a list 
only as long as the number of words that the user inputs.

'''

with open("/usr/share/dict/words", "r") as myfile:  #opens file
	word_list = myfile.read()						#stores reading file into word_list

def generate_word(number):

	sentence = ""
	
	for i in range(number): #repeats for input number of times
		
		lines = word_list.splitlines() #creates list of words and stores them in lines
		line_number = random.randrange(0, len(lines)) #generates random number between 0 and 
		word = lines[line_number]  #gets words @ random index  		 #the length of the list

		if i == number - 1: #if the number is less than the number inputed
			sentence += (word + "!") #concatenate sentence with new word
		else:
			sentence += (word + " ") 

	return sentence
	
	

if __name__ == '__main__':
	input_args = sys.argv[1] 
	sentence_length = int(input_args) #setting sentence length equal to input length

	sentence = generate_word(sentence_length)
	print(sentence)