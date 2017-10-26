import random
import sys
import time

'''

Takes file of words from local directory and puts them in a list 
only as long as the number of words that the user inputs.

'''

with open("/usr/share/dict/words", "r") as myfile:  #opens file
	word_list = myfile.read().splitlines()						#stores reading file into word_list

def generate_word(number):



	phrase = ""
	
	for i in range(number): #repeats for input number of times
		
		line_number = random.randrange(0, len(word_list)) #generates random number between 0 and 
		word = word_list[line_number]  #gets words @ random index  		  #the length of the list

		if i == number - 1: #if the number is less than the number inputed
			phrase += (word + "!") #concatenate sentence with new word
		else:
			phrase += (word + " ") 
	
	return phrase
	
	

if __name__ == '__main__':
	time_one = time.time() 
	input_args = sys.argv[1] 
	phrase_length = int(input_args) #setting sentence length equal to input length
	phrase = generate_word(phrase_length)
	print(phrase)
	final_time = time.time() - time_one
	print(final_time)



