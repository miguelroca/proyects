#!/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')

def helloworld():
	return '!!Hola clase de CDK'
	
@app.route('/saludo/<persona>')
def saludoDinamico(persona):
	return 'Hola %s, bienvenido!!!' % persona
	
if __name__ == "__main__";
	app.run(host = "0.0.0.0", port = 3001, debug = True)