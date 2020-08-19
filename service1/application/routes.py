from flask import Flask, request, jsonify
from application import app
from random import randint
import random 
import requests



@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", title="Home")


@app.route("/generate", methods=['GET','POST'])
def animal():
    animal_response = requests.get("http://35.189.85.195:5001/get/animal")
    animal1 = animal_response.json()["animal"]
    # animal1 = animal1["animal"]
    noise_reponse = requests.post("http://35.189.85.195:5001/get/noise", json={"animal": animal1})
    noise1 = animal_response.json()["noise"]
    return render_template("generate.html", animal= animal1, noise=noise1)
    
