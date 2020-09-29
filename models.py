from flask_serialize import FlaskSerializeMixin

from app import db, ma,fields,Schema  

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


class Ciudad(db.Model):
     __tablename__ = 'city'
     city_id = db.Column(db.Integer,primary_key=True)
     city = db.Column(db.String())
     country_id = db.Column(db.Integer,db.ForeignKey('country_id'))
     last_update = db.Column(db.String())
     def __init__(self,city,country_id,last_update):
          self.city = city
          self.country_id =country_id
          self.last_update =last_update
     def __repr__(self):
          return 'city_id{}'.format(self.city_id)     


class ResultSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
          model = Result
          load_instance =True
class Address(db.Model):
     __tablename__ = 'address'
     address_id = db.Column(db.Integer,primary_key=True)
     address = db.Column(db.String())
     address2 = db.Column(db.String())
     district = db.Column(db.String())
     city_id = db.Column(db.Integer,db.ForeignKey('city_id'))
     postal_code = db.Column(db.String())
     phone = db.Column(db.String())
     last_update = db.Column(db.String())
     


class Empleado(db.Model):
     __tablename__ = 'customer'
     customer_id = db.Column(db.Integer,primary_key=True)
     store_id = db.Column(db.Integer,db.ForeignKey('store_id'))
     first_name = db.Column(db.String())
     last_name = db.Column(db.String())
     email = db.Column(db.String())
     address_id =db.Column(db.Integer,db.ForeignKey(Address.address_id))
     activebool = db.Column(db.Boolean)
     create_date = db.Column(db.String())
     last_update = db.Column(db.String())
     active = db.Column(db.Integer())
     cucuy = db.relationship('Address',backref="direccion")
    

class AddressSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
           model = Address
           load_instance =True

class EmpleadoSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
          model = Empleado
          load_instance =True
          
              

           
    
     




