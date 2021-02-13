#!/bin/python

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, clase de CDK!!'
	
@app.route('/saludo/<persona>')
def saludoDinamico(persona):
	return 'Hola %s, bienvenido!!!' % persona

@app.route('/test', methods=['POST', 'GET'])
def recibeParams():
	textReturn = "Método no aceptado"
	if request.method == "POST":
		data = request.get_json()
		try:
			mascota = data['mascota']
			textReturn = 'Se recibió: %s' % mascota
		except:
			textReturn = "Ocurrió un error"
	return textReturn
	
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 3000, debug = True)

