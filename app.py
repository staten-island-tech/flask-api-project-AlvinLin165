from flask import Flask,
import requests

app = Flask(__name__)

@app.route("/")
def brazilian():
    cars = []
    response= requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")
    vehicle = response.json()
    


    brazil_car= vehicle['results']
    for cars in brazil_car:
        url = cars['url']
        