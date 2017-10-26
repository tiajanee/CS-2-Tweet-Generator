import random

'''
Generates words from pre-defined list and shuffles at script call in terminal.

'''

def rearrange_Word():
	
	quotes = ["beam", "me", "up", "scotty"]
	random.shuffle(quotes) #shuffles items in list
	return quotes

if __name__ == '__main__':
	quote = rearrange_Word()
	print(quote)