from flask import Flask
from flask import send_from_directory
from flask import flash, redirect, render_template, request, session, abort, url_for
import os
import random
import factract
from card import make_card
from imgpil import create_imgs


app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.errorhandler(400)
def badreq(e):
	return render_template('400.html')

@app.route('/')
def home():
	#return render_template('index.html')
	return render_template('index.html')

@app.route('/fact', methods = ['GET','POST'])
def fact():
	global user_input
	user_input = request.form['user_input']
	img_url = factract.get_image(user_input)
	card_text = make_card(user_input)
	# print card_text
	# text = sat_extract.fact_extract(user_input)
	text = factract.factract(user_input).decode('utf-8')
	if text=='':
		return "Working	"
	text = text.split('\n')
	return render_template('profile.html', text = text, img_url = img_url, user_input = user_input, card_text=card_text)

@app.route('/images',methods=['GET'])
def img():
	img_list=create_imgs(user_input)
	print len(img_list)
	return render_template('image.html',images=img_list)


if __name__ == "__main__":
	app.run(port=8080)
