from app.extensions.database import db 
from app.models.orders import Foto

def test_foto_update(client): 
    #updates foto's properties
    foto = Foto(id=26, slug='caro-1', name='caro', price=25,picture_url='../static/images/portrait/caro-1.jpg', genre='portrait', country='None', city='nada')
    db.session.add(foto)
    db.session.commit()

    foto.price = 25
    foto.save()

    updated_foto = Foto.query.filter_by(slug='caro-1').first()
    assert updated_foto.price == 25


def test_foto_delete(client): 
    # delete a foto
    foto = Foto(id=26, slug='caro-1', name='caro', price=25,picture_url='../static/images/portrait/caro-1.jpg', genre='portrait', country='None', city='nada')

    foto.delete()

    deleted_foto = Foto.querry.filter_by(slug='caro-1').first()
    assert deleted_foto is None