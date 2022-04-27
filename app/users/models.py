from app.extensions.database import CRUDMixin, db
from flask_login import UserMixin

class User(db.Model, CRUDMixin, UserMixin): 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(80), index = True)
    password = db.Column(db.String(120))
    orders = db.relationship('Order', backref='user')
