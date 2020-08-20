from flask import Flask, request, jsonify, render_template
from application import app
from random import randint
import random 
import requests



@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", title="Home")


@app.route("/generate", methods=['GET','POST'])
def animal():
    animal_response = requests.get("http://34.105.242.163:5001/get/animal")
    animal1 = animal_response.json()
    animal2 = animal1["animal"]
    noise_response = requests.post("http://34.105.242.163:5001/get/noise", json={"animal": animal2})
    noise1 = noise_response.json()
    noise2 = noise1["noise"]

    return render_template("generate.html", animal= animal2, noise=noise2)
    
