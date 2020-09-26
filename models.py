from app import db   

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
