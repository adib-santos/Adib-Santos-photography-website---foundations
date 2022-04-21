from app.extensions.database import CRUDMixin, db

class User(db.Model, CRUDMixin): 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(80), index = True, primary_key = True)
    password = db.Column(db.String(120))
