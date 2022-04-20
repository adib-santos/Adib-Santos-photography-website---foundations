from app.extensions.database import db 
from app.models.orders import Foto



def test_foto_update(client): 
    # updates foto's properties
    foto  = Foto(slug = 'choco', name = 'chocolate', price = 12)
    db.session.add(foto)
    db.session.commit()

    foto.name = 'vainilla'
    foto.save()

    updated_foto = Foto.query.filter_by(slug='choco').first()
    assert updated_foto.name == 'vainilla'


def test_cookie_delete(client):
  # deletes cookie
  foto = Foto(slug='butter', name='Butter', price=1.50)
  db.session.add(foto)
  db.session.commit()

  foto.delete()

  deleted_foto = Foto.query.filter_by(slug='butter').first()
  assert deleted_foto is None
