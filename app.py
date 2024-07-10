from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

with app.app_context(): 
  
  app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///greetings.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


  db = SQLAlchemy(app)
  ma = Marshmallow(app)


  ########################## START MODELS AND SCHEMA ####################

  class Greeting(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(50))
    language = db.Column(db.String(20),  nullable=True)
    
    def __init__(self, msg, lang):
      self.message = msg
      self.language = lang
      
  db.create_all()


  class GreetingSchema(ma.Schema):
    class Meta:
      fields = ('id', 'message', 'language')

  greeting_schema = GreetingSchema()
  greetings_schema = GreetingSchema(many=True)
  
  ########################## END MODELS AND SCHEMA ####################


  ########################### START  ROUTES ###########################

  # Create greeting
  @app.route('/saludos', methods=['POST'])
  def createGreeting():
    message = request.json['message']
    lang = request.json['language']
    
    if message and message != "":
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
