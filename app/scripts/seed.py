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
        'price': 30, 'picture_url': '../static/images/portrait/caro-1.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Tumbaco',
       },
   'caro_2' : {
        'id': 2,
        'name': 'caro-2', 
        'price': 30, 'picture_url': '../static/images/portrait/caro-2.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Tumbaco',
       },
   'chicky-1' : {
        'id': 3,
        'name': 'chicky', 
        'price': 30, 'picture_url': '../static/images/portrait/chicky-1.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
       },
   'churos-3' : {
        'id': 4,
        'name': 'churos-3', 
        'price': 30, 'picture_url': '../static/images/portrait/churos-3.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Cumbaya',
       },
   'franco-1' : {
        'id': 5,
        'name': 'franco-1', 
        'price': 30, 'picture_url': '../static/images/portrait/franco-1.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Cumbaya',
       },
   'franco-2' : {
        'id': 6,
        'name': 'franco-2', 
        'price': 30, 'picture_url': '../static/images/portrait/franco-2.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Cumbaya',
       },
   'franco-3' : {
        'id': 7,
        'name': 'franco-3', 
        'price': 30, 'picture_url': '../static/images/portrait/franco-3.jpg',
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Cumbaya',
       },
    'churos-1' : {
        'id': 8,
        'name': 'churos-1',
        'price': 30, 'picture_url': '../static/images/portrait/churos-1.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'jaz1' : {
        'id': 9,
        'name': 'jaz-1',
        'price': 30, 'picture_url': '../static/images/portrait/jaz1.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'jaz2' : {
        'id': 10,
        'name': 'jaz2',
        'price': 30, 'picture_url': '../static/images/portrait/jaz2.jpg', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Quito',
    },
    'isa' : {
        'id': 11,
        'name': 'isa',
        'price': 30, 'picture_url': '../static/images/portrait/isa.JPG', 
        'genre': 'portrait', 'country': 'Ecuador', 'city': 'Casablanca',
    },


                                # STREET part of the database


    'flamingo' : {
        'id': 12,
        'name': 'flamingo', 
        'price': 40, 'picture_url': '../static/images/street/flamingo.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Galapagos',
       },
    'fern-bg' : {
        'id': 13,
        'name': 'fern-bg', 
        'price': 40, 'picture_url': '../static/images/street/fern-bg.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Tumbaco',
       },
    'covid-child' : {
        'id': 14,
        'name': 'covid-child', 
        'price': 40, 'picture_url': '../static/images/street/covid-child.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Quito',
       },
    'caught_telaviv' : {
        'id': 15,
        'name': 'caught_telaviv', 
        'price': 40, 'picture_url': '../static/images/street/caught_telaviv.jpg',
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv',
       },
    'big-contrast-akko' : {
        'id': 16,
        'name': 'big-contrast-akko', 
        'price': 40, 'picture_url': '../static/images/street/big-contrast-akko.jpg',
        'genre': 'street', 'country': 'Israel', 'city': 'Akko',
       },
   'ingvildsita' : {
        'id': 17,
        'name': 'ingvildsita', 
        'price': 30, 'picture_url': '../static/images/street/ingvildsita.jpg',
        'genre': 'street', 'country': 'Czech Republic', 'city': 'Prague',
       },
    'mama-mia' : {
        'id': 18,
        'name': 'mama-mia', 
        'price': 40, 'picture_url': '../static/images/street/mama-mia.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'hija-con-su-hija' : {
        'id': 19,
        'name': 'hija-con-su-hija', 
        'price': 40, 'picture_url': '../static/images/street/hija-con-su-hija.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Tumbaco',
       },
   'news' : {
        'id': 20,
        'name': 'news', 
        'price': 30, 'picture_url': '../static/images/street/news.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-2-color' : {
        'id': 21,
        'name': 'reflection-2-color', 
        'price': 25, 'picture_url': '../static/images/street/reflection-2-color.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'reflection-2' : {
        'id': 22,
        'name': 'reflection-2', 
        'price': 25, 'picture_url': '../static/images/street/reflection-2.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'grapes' : {
        'id': 23,
        'name': 'grapes', 
        'price': 25, 'picture_url': '../static/images/street/grapes.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'sleepless' : {
        'id': 24,
        'name': 'sleepless', 
        'price': 25, 'picture_url': '../static/images/street/sleepless.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
    'tren-telaviv' : {
        'id': 25,
        'name': 'tren-telaviv', 
        'price': 25, 'picture_url': '../static/images/street/train_telaviv.jpg',
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv',
       },
    'vacas' : {
        'id': 26,
        'name': 'vacas', 
        'price': 25, 'picture_url': '../static/images/street/vacas.jpg',
        'genre': 'street', 'country': 'Ecuador', 'city': 'Papallacta',
       },
   'fisherman' : {
        'id': 27,
        'name': 'fisherman', 
        'price': 30, 'picture_url': '../static/images/street/fisherman.jpg',
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
       },
}



for key, value in fotos_db.items():
    new_foto = Foto(name=fotos_db[key]['name'], id = fotos_db[key]['id'], price=fotos_db[key]['price'], picture_url=fotos_db[key]['picture_url'], genre=fotos_db[key]['genre'], country=fotos_db[key]['country'], city=fotos_db[key]['city'])
    db.session.add(new_foto)

db.session.commit()
# db.session.refresh(new_foto)