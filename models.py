from app import db, ma

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