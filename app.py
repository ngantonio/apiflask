from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import environ
import json

app = Flask(__name__)

with app.app_context(): 
  
  app.config['SQLALCHEMY_DATABASE_URI'] =  environ.get("DB_URL")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


  db = SQLAlchemy(app)
  ma = Marshmallow(app)

  # import model and schemas
  from models import Greeting, greeting_schema, greetings_schema

  ########################### START  ROUTES ###########################
  
  # Create greeting
  @app.route('/saludos', methods=['POST'])
  def createGreeting():
    data = json.loads(request.data)
   
    if 'language' in data:
      lang = data['language']
    else:
      lang = ""
    
    if 'message' in data and data['message'] != "":
      message = data['message']
      new_greeting = Greeting(message,lang)
      db.session.add(new_greeting)
      db.session.commit()
      return greeting_schema.jsonify(new_greeting)
    return jsonify({"message": "El mensaje es requerido para almacenar el saludo"}),404
    
    
  # Get greetings
  @app.route('/saludos', methods=['GET'])
  def getGreetings():
    all_greetings = Greeting.query.all()
    return jsonify(greetings_schema.dump(all_greetings))
  

  # Get greeting by id
  @app.route('/saludos/<id>', methods=['GET'])
  def getGreeting(id):
    greeting = Greeting.query.get(id)
    
    if greeting:
      return greeting_schema.jsonify(greeting)
    return jsonify({"message": "El saludo requerido no existe"}),404
  
  
  # Update greeting
  @app.route('/saludos/<id>', methods=['PUT'])
  def updateGreeting(id):
    
    greeting = Greeting.query.get(id)
    
    if greeting:
      updatedMsg = request.json['message']
      updatedLang = request.json['language']
    
      if updatedMsg and updatedMsg != "":   
        greeting.message = updatedMsg
        greeting.language = updatedLang
        db.session.commit()
    
        return greeting_schema.jsonify(greeting)
      
      return jsonify({"message": "El mensaje es requerido para almacenar el saludo"}),404
    return jsonify({"message": "El saludo requerido no existe"}),404
  

  # Delete greeting
  @app.route('/saludos/<id>', methods=['DELETE'])
  def deleteGreeting(id):
    
    greeting = Greeting.query.get(id)
    
    if greeting:
      db.session.delete(greeting)
      db.session.commit()
      return greeting_schema.jsonify(greeting)
    return jsonify({"message": "El saludo requerido no existe"}),404
    

 ########################### END ROUTES ################################
