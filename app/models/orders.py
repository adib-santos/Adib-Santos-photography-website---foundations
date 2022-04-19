from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Order(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
  adress_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable = False)
  foto_id = db.Column(db.Integer, db.ForeignKey('foto.id'), nullable = False)
  users = db.relationship('User', backref='order', lazy=True)

class Address(db.Model, CRUDMixin):     
  id = db.Column(db.Integer, primary_key = True)
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))
  orders = db.relationship('Order', backref = 'address', lazy = True)

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
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = False)

  

#   slug = db.Column(db.String(80), unique = True)
