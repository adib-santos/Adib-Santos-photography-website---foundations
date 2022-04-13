from app.extensions.database import db
from datetime import datetime

class Order(db.Model): 
  id = db.Column(db.Integer, primary_key = True)
  date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
  address = db.relationship('Address', backref = 'order', uselist = False, lazy = True)

class Address(db.Model):     
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80))
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))
  order_id = db.Column(db.Integer, db.ForeignKey('order.id')) # Connection to order

class Foto(db.Model): 
  id = db.Column(db.String(80), primary_key = True)
  slug = db.Column(db.String(80), unique = True)
  price = db.Column(db.Numeric(10, 2))
  picture_url = db.Column(db.String(80))
  genre = db.Column(db.String(80))
  country = db.Column(db.String(80))
  city = db.Column(db.String(80))

