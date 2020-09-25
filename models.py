from app import db   

class Result(db.Model):
     __tablename__ = 'country'
     id = db.Column(db.Integer,primary_key=True)
     pais = db.Column(db.String())
     fehca = db.Column(db.String())
     def __init__(self,pais,fehca):
          self.pais = pais
          self.fehca = fehca
     def __repr__(self):
         return '<id{}>'.format(self.id)      
