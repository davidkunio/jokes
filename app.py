from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('main.html')

@app.route('/joke', methods=['POST'])
def joke():
	error = None
	if request.method!= 'POST':
		error = 'Unable to make a joke! LAME'
	else:
		noun = request.form['noun']
		adverb = request.form['adverb']
		adjective = request.form['adjective']
		verb = request.form['verb']
		
		#number_of_jokes = bake_cookie(noun + adverb + adjective + verb, request, response)

		return render_template('joke_output.html', noun=noun, adjective=adjective, adverb=adverb, verb=verb)
	return render_template('main.html', error = error)
'''
def bake_cookie(joke, request, response):
	uniq_jokes_cookie = request.cookies.get('unique_jokes')
	unique_jokes = uniq_jokes_cookie['jokes']

	if joke not in unique_jokes:
		unique_jokes.append(joke)
		response.set_cookie('unique_jokes', unique_jokes)

	return len(unique_jokes) if unique_jokes else 0
'''
if __name__ == "__main__":
    app.run(debug = True)