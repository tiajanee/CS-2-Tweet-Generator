import random

'''
Outputs random words from a Tuple.

'''

quotes = ("Winter is Coming!", 
	"There! Beyond the Wall!", "I am the heir to the Iron Throne!") #creates list of quotes

def random_GOT_quote():
	rand_index = random.randint(0, len(quotes) -1) #creates random index as long as length 
	return quotes[rand_index] 					   #of items in list

if __name__ == '__main__':
	quote = random_GOT_quote()
	print(quote)