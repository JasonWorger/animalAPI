from flask import Flask, request, jsonify
from application.models import Animal
from application import app, db
from random import randint
import random 
 
@app.route('/')
@app.route('/get/animal', methods=['GET'])
def animal():
 animal1 = Animal.query.filter_by(id=randint(1,4)).first()
 return jsonify({'animal':animal1.animal})
 
@app.route('/get/noise', methods=['GET','POST'])
def noise():
 data_sent = request.get_json()
 noise1 = Animal.query.filter_by(animal=data_sent['animal']).first()
 return jsonify({'noise':noise1.noise})