# This file holds all aditions that come from 3rd party packages

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # -> Why is this not importing properly?


db = SQLAlchemy()
migrate = Migrate()


class CRUDMixin(): 

    def save(self): 
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self): 
        db.session.delete(self)
        db.session.commit()
        return