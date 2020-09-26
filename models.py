from flask_serialize import FlaskSerializeMixin

from app import db, ma  

class Result(db.Model):
     __tablename__ = 'country'
     country_id = db.Column(db.Integer,primary_key=True)
     country = db.Column(db.String())
     last_update = db.Column(db.String())
     def __init__(self,country,last_update):
          self.country = country
          self.last_update = last_update
     def __repr__(self):
         return '<country_id{}>'.format(self.country_id)      

class Pais(FlaskSerializeMixin,db.Model):
     _tablename__ = 'country'
     country_id = db.Column(db.Integer,primary_key=True)
     country = db.Column(db.String())
     last_update = db.Column(db.String())
     #serializar campos
     
     crear_campos = update_fields =['country_id','country','last_update']
     # checks if Flask-Serialize can create/update
     def __init__(self,country,last_update):
          self.country = country
          self.last_update = last_update
     def __repr__(self):
         return '<country_id{}>'.format(self.country_id)

class ResultSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
          model = Result
          load_instance =True