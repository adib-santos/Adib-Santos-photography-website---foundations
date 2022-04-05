from turtle import update
from app.extensions.database import db
from app.shop_outer.models import Foto

def test_foto_update(client): 
    # updates foto's properties
    foto = Foto(slug="Valencia", name="massi", price=30)
    db.session.add(foto)
    db.session.commit()

    foto.name = "donna"
    foto.save()

    update_foto = Foto.query.filter_by(slug = "Valencia").first()
    assert update_foto.name == "donna"

def test_foto_delete(client):
    # deletes foto
    foto = Foto(slug="Valencia", name="massi", price=30)
    db.session.add(foto)
    db.session.commit()

    foto.delete()

    deleted_foto = Foto.query.filter_by(slug="Valencia").first()
    assert deleted_foto is None
