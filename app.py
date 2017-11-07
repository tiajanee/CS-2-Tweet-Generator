from flask import Flask
import histogram 

app = Flask(__name__)

@app.route('/')
def lol():
	text_file = open('practice_text.txt')
	text_word_list = [word.lower() for word in text_file.read().rsplit()]
	text_histogram = histogram.histogram(text_word_list)
	return histogram.random_word(text_histogram)

