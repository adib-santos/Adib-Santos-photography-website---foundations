from app.app import create_app
from app.models.orders import Foto
from app.extensions.database import db

app = create_app()
app.app_context().push() # -> gives me access to the flask app

fotos_db = {
                        # PORTRAIT Part of the database
    'caro_1' : {
        'id': 1,
        'name': 'caro', 
        'price': 25, 'picture_url': '../static/images/portrait/caro-1.jpg',
        'genre': 'portrait', 'country': 'nada', 'city': 'nada',
       },
   'caro_2' : {
        'id': 2,
        'name': 'caro-2', 
        'price': 25, 'picture_url': '../static/images/portrait/caro-2.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
   'chicky-1' : {
        'id': 3,
        'name': 'chicky', 
        'price': 25, 'picture_url': '../static/images/portrait/chicky-1.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
   'churos-2' : {
        'id': 4,
        'name': 'churos-2', 
        'price': 25, 'picture_url': '../static/images/portrait/churos-2.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
   'churos-3' : {
        'id': 5,
        'name': 'churos-3', 
        'price': 25, 'picture_url': '../static/images/portrait/churos-3.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
   'franco-1' : {
        'id': 6,
        'name': 'franco-1', 
        'price': 25, 'picture_url': '../static/images/portrait/franco-1.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
   'franco-2' : {
        'id': 7,
        'name': 'franco-2', 
        'price': 25, 'picture_url': '../static/images/portrait/franco-2.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
   'franco-3' : {
        'id': 8,
        'name': 'franco-3', 
        'price': 25, 'picture_url': '../static/images/portrait/franco-3.jpg',
        'genre': 'portrait', 'country': 'None', 'city': 'None',
       },
    'churos-1' : {
        'id': 9,
        'name': 'churos-1',
        'price': 25, 'picture_url': '../static/images/portrait/churos-1.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'jaz1' : {
        'id': 10,
        'name': 'jaz-1',
        'price': 25, 'picture_url': '../static/images/portrait/jaz1.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'lucy' : {
        'id': 11,
        'name': 'lucy',
        'price': 25, 'picture_url': '../static/images/portrait/lucy.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'jaz2' : {
        'id': 12,
        'name': 'jaz2',
        'price': 25, 'picture_url': '../static/images/portrait/jaz2.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'isa' : {
        'id': 13,
        'name': 'isa',
        'price': 25, 'picture_url': '../static/images/portrait/isa.JPG', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },


                                # STREET part of the database
    'lonely_telaviv' : {
        'id': 14,
        'name': 'lonely-telaviv', 
        'price': 25, 'picture_url': '../static/images/street/lonely_telaviv.jpg',
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv',
       },
    'mama-mia' : {
        'id': 15,
        'name': 'mama-mia', 
        'price': 25, 'picture_url': '../static/images/street/mama-mia.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
   'news' : {
        'id': 16,
        'name': 'news', 
        'price': 25, 'picture_url': '../static/images/street/news.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-1' : {
        'id': 17,
        'name': 'reflection-1', 
        'price': 25, 'picture_url': '../static/images/street/reflection-1.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-1-color' : {
        'id': 18,
        'name': 'reflection-1-color', 
        'price': 25, 'picture_url': '../static/images/street/reflection-1-color.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-2-color' : {
        'id': 19,
        'name': 'reflection-2-color', 
        'price': 25, 'picture_url': '../static/images/street/reflection-2-color.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-2' : {
        'id': 20,
        'name': 'reflection-2', 
        'price': 25, 'picture_url': '../static/images/street/reflection-2.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-3-color' : {
        'id': 21,
        'name': 'reflection-3-color', 
        'price': 25, 'picture_url': '../static/images/street/reflection-3-color.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-3' : {
        'id': 22,
        'name': 'reflection-3', 
        'price': 25, 'picture_url': '../static/images/street/reflection-3.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-rome' : {
        'id': 23,
        'name': 'reflection-rome', 
        'price': 25, 'picture_url': '../static/images/street/reflection-rome.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'shop-owner-1' : {
        'id': 24,
        'name': 'show-owner-1', 
        'price': 25, 'picture_url': '../static/images/street/shop-owner-1.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'sleepless' : {
        'id': 25,
        'name': 'sleepless', 
        'price': 25, 'picture_url': '../static/images/street/sleepless.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'street-main-1' : {
        'id': 26,
        'name': 'street-main-1', 
        'price': 25, 'picture_url': '../static/images/street/street-main.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'tren-telaviv' : {
        'id': 27,
        'name': 'tren-telaviv', 
        'price': 25, 'picture_url': '../static/images/street/train_telaviv.jpg',
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv',
       },
    'vacas' : {
        'id': 28,
        'name': 'vacas', 
        'price': 25, 'picture_url': '../static/images/street/vacas.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Papallacta',
       },
    'vertical-reflection' : {
        'id': 29,
        'name': 'vertical-reflection', 
        'price': 25, 'picture_url': '../static/images/street/vertical-reflection.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Papallacta',
       }, 
}



for key, value in fotos_db.items():
    new_foto = Foto(name=fotos_db[key]['name'], id = fotos_db[key]['id'], price=fotos_db[key]['price'], picture_url=fotos_db[key]['picture_url'], genre=fotos_db[key]['genre'], country=fotos_db[key]['country'], city=fotos_db[key]['city'])
    db.session.add(new_foto)

db.session.commit()
# db.session.refresh(new_foto)