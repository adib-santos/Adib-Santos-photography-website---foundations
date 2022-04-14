from app.app import create_app
from app.models.orders import Foto
from app.extensions.database import db

app = create_app()
app.app_context().push() # -> gives me access to the flask app

fotos_db = {
    'chicky-1' : {
        'id': 3, 
        'slug': 'chicky-1',
        'price': 25, 'picture_url': '/static/images/street/chicky-1.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Quito',
    },
}



for key, value in fotos_db.items():
    new_foto = Foto(slug=fotos_db[key]['slug'], id = fotos_db[key]['id'], price=fotos_db[key]['price'], picture_url=fotos_db[key]['picture_url'], genre=fotos_db[key]['genre'], country=fotos_db[key]['country'], city=fotos_db[key]['city'])
    db.session.add(new_foto)

db.session.commit()
db.session.refresh(new_foto)