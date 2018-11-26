import os

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def checkCar():
    return "controller.checkCar()"
    

app.run("0.0.0.0",3000,True)