from app.extensions.database import db, CRUDMixin

class Order(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  street = db.Column(db.String(80))
  city = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  country = db.Column(db.String(80))
  foto_id = db.Column(db.Integer, db.ForeignKey('foto.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Foto(db.Model, CRUDMixin): 
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), unique = True)
  price = db.Column(db.Numeric(10, 2))
  picture_url = db.Column(db.String(80))
  genre = db.Column(db.String(80))
  country = db.Column(db.String(80))
  city = db.Column(db.String(80))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  orders = db.relationship('Order', backref='foto')







 