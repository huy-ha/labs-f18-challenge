from flask import Flask, render_template
import requests
import json
import re

app = Flask(__name__)


@app.route('/pokemon/<variable>', methods=['GET'])
def main(variable):
	url = 'http://pokeapi.co/api/v2/pokemon/' + variable
	r = requests.get(url)
	url = r.json()['forms'][0]['url']
	name = r.json()['forms'][0]['name']
	id = re.search('(?<=pokemon-form\/)\d+',url).group(0)

	
	if variable.isdigit():
		value = "The pokemon with id " + id + " is " + name
	else:
		value = name + " has id " + id
	return render_template('index.html',value = value)


if __name__ == '__main__':
    app.run()