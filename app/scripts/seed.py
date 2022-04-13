from venv import create
from app.app import create_app
from app.models.base import Foto
from app.extensions.database import db

app = create_app()
app.app_context().push() # -> gives me access to the flask app

fotos_db = {
                                # This is the PORTRAIT part of the database
    'caro_1' : {
        'price': 25, 'picture_url': '/static/images/portrait/caro-1.jpg', 
        'genre': 'portrait', 'country': 'nada', 'city': 'nada', 
        },
    'caro_2' : {
        'price': 25, 'picture_url': '/static/images/portrait/caro-2.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'chicky-1' : {
        'price': 25, 'picture_url': '/static/images/portrait/chicky-1.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'churos-1' : {
        'price': 25, 'picture_url': '/static/images/portrait/churos-1.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'churos-2' : {
        'price': 25, 'picture_url': '/static/images/portrait/churos-2.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'churos-3' : {
        'price': 25, 'picture_url': '/static/images/portrait/churos-3.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'franco-1' : {
        'price': 25, 'picture_url': '/static/images/portrait/franco-1.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'franco-2' : {
        'price': 25, 'picture_url': '/static/images/portrait/franco-2.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'franco-3' : {
        'price': 25, 'picture_url': '/static/images/portrait/franco-3.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'isa' : {
        'price': 25, 'picture_url': '/static/images/portrait/isa.JPG', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'jaz1' : {
        'price': 25, 'picture_url': '/static/images/portrait/jaz1.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'jaz2' : {
        'price': 25, 'picture_url': '/static/images/portrait/jaz2.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },   
    'lucy' : {
        'price': 25, 'picture_url': '/static/images/portrait/lucy.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'memi-1' : {
        'price': 25, 'picture_url': '/static/images/portrait/memi-1.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'shapo-1' : {
        'price': 25, 'picture_url': '/static/images/portrait/shapo-1.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },
    'shapo-2' : {
        'price': 25, 'picture_url': '/static/images/portrait/shapo-2.jpg', 
        'genre': 'portrait', 'country': 'None', 'city': 'None', 
        },            
                                        # This is the STREET part of the database

    'aaron' : {
        'price': 25, 'picture_url': '/static/images/street/aaron.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Haifa', 
        },   
    'big-contrast-akko' : {
        'price': 25, 'picture_url': '/static/images/street/big-contrast-akko.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Akko', 
        },  
    'caught_telaviv' : {
        'price': 25, 'picture_url': '/static/images/street/caught_telaviv.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv', 
        }, 
    'covid-child' : {
        'price': 25, 'picture_url': '/static/images/street/covid-child.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Haifa', 
        }, 
    'covid-child' : {
        'price': 25, 'picture_url': '/static/images/street/covid-child.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Haifa', 
        }, 
    'fern-bg' : {
        'price': 25, 'picture_url': '/static/images/street/fern-bg.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Tumbaco', 
        }, 
    'flamingo' : {
        'price': 25, 'picture_url': '/static/images/street/flamingo.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Galapagos', 
        }, 
    'framed-haifa' : {
        'price': 25, 'picture_url': '/static/images/street/framed-haifa.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Haifa', 
        }, 
    'grapes' : {
        'price': 25, 'picture_url': '/static/images/street/grapes.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Tumbaco', 
        }, 
    'haifa-berries' : {
        'price': 25, 'picture_url': '/static/images/street/haifa-berries.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Haifa', 
        }, 
    'height-contrast-color' : {
        'price': 25, 'picture_url': '/static/images/street/height-contrast-color.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome', 
        }, 
    'grapes' : {
        'price': 25, 'picture_url': '/static/images/street/grapes.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Tumbaco', 
        }, 
    'height-contrast' : {
        'price': 25, 'picture_url': '/static/images/street/height-contrast.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome', 
        }, 
    'hija-con-su-hija' : {
        'price': 25, 'picture_url': '/static/images/street/hija-con-su-hija.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Quito', 
        },
    'ingvildsita' : {
        'price': 25, 'picture_url': '/static/images/street/ingvildsita.jpg', 
        'genre': 'street', 'country': 'Czech Republic', 'city': 'Prague',
        },
    'lonely_telaviv' : {
        'price': 25, 'picture_url': '/static/images/street/lonely_telaviv.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv',
        },
    'mama-mia' : {
        'price': 25, 'picture_url': '/static/images/street/mama-mia.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'mama-mia' : {
        'price': 25, 'picture_url': '/static/images/street/mama-mia.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'news' : {
        'price': 25, 'picture_url': '/static/images/street/news.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-1' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-1.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-1-color' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-1-color.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-1' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-1.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-2-color' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-2-color.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-2' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-2.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-3-color' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-3-color.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-3' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-3.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'reflection-rome' : {
        'price': 25, 'picture_url': '/static/images/street/reflection-rome.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'shop-owner-1' : {
        'price': 25, 'picture_url': '/static/images/street/shop-owner-1.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'sleepless' : {
        'price': 25, 'picture_url': '/static/images/street/sleepless.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'street-main-1' : {
        'price': 25, 'picture_url': '/static/images/street/street-main.jpg', 
        'genre': 'street', 'country': 'Italy', 'city': 'Rome',
        },
    'tren-telaviv' : {
        'price': 25, 'picture_url': '/static/images/street/train_telaviv.jpg', 
        'genre': 'street', 'country': 'Israel', 'city': 'Tel Aviv',
        },
    'vacas' : {
        'price': 25, 'picture_url': '/static/images/street/vacas.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Papallacta',
        },
    'vertical-reflection' : {
        'price': 25, 'picture_url': '/static/images/street/vertical-reflection.jpg', 
        'genre': 'street', 'country': 'Ecuador', 'city': 'Papallacta',
        },

}


for slug, foto in fotos_db.items():
    new_foto = Foto(slug=slug, picture_url=foto['picture_url'], price=foto['price'], genre=foto['genre'], country=foto['country'], city=foto['city'])
    db.session.add(new_foto)

db.session.commit()