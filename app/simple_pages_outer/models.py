from enum import unique
from app.extensions.database import db # -> imports the ORM 


class Street(): 
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(80), unique = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Numeric(10, 2))