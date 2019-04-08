import os
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from jinja2 import Template
from spellchecker import SpellChecker

app = Flask(__name__)

# @app.route('/')

@app.route('/spellCorrect/<word>')
def spellCorrect(word):
	if len(word) < 8:
		spell = SpellChecker()
	else:
		spell = SpellChecker(distance=2)

	#if word is mispelled
	if spell[word] == 0:
		# Get a list of `likely` options
		print(spell.candidates(word))
	
	return spell.candidates(word)

	#below code can be used to upload word frequency of custom text file
	#spell.word_frequency.load_text_file('./path-to-my-text-doc.txt')

if __name__ == '__main__':
	app.run(debug=False)
