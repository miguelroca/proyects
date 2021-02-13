#!/bin/python

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route('/')
def hello_world():
    count = redis.incr("consultas")
    return '¡Bienvenid@! Veces que se ha consultado este sitio: {} \n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

