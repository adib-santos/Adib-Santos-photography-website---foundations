from app.extensions.database import CRUDMixin, db

class User(db.Model, CRUDMixin): 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), index = True, unique = True)
    password = db.Column(db.String(120))