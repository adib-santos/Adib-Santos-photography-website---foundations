from turtle import update
from app.extensions.database import db
from app.simple_pages_outer.models import Street

def test_foto_update(client): 
    # updates foto's properties
    foto = Street(slug="Valencia", name="massi", price=30)
    db.session.add(foto)
    db.session.commit()

    foto.name = "donna"
    foto.save()

    update_foto = Street.query.filter_by(slug = "Valencia").first()
    assert update_foto.name == "donna"

def test_foto_delete(client):
    # deletes foto
    foto = Street(slug="Valencia", name="massi", price=30)
    db.session.add(foto)
    db.session.commit()

    foto.delete()

    deleted_foto = Street.query.filter_by(slug="Valencia").first()
    assert deleted_foto is None
