from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Order(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  foto_id = db.Column(db.Integer, db.ForeignKey('foto.id'), nullable = False)
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))

class Foto(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  slug = db.Column(db.String(80), unique = True)
  name = db.Column(db.String(80), unique = True)
  price = db.Column(db.Numeric(10, 2))
  picture_url = db.Column(db.String(80))
  genre = db.Column(db.String(80))
  country = db.Column(db.String(80))
  city = db.Column(db.String(80))
  orders = db.relationship('Order', backref='foto', lazy = True)
  

class User(db.Model): 
  id = db.Column(db.Integer, primary_key = True)
  slug = db.Column(db.String(80), unique = True)
  name = db.Column(db.String(80))
  password = db.Column(db.String(80))

  
# This column is supposed to go in Order:   
# date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
