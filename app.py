from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/')

def main():
	return render_template('index.html')
	@app.route('/', methods=['POST'])

	def mathOp():
		equation = request.form['text']
		operation = request.form['operation']
		calc =  'https://newton.now.sh/api/v2//' + operation + '/' + equation
		result = requests.get(result).json()
		answer = result['result']
		return render_template('index.html', result=answer, equation=equation)

if __name__ == '__main__':
	app.run() 