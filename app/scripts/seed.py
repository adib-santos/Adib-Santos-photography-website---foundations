from app.app import create_app
from app.shop_outer.models import Foto
from app.extensions.database import db

app = create_app()
app.app_context().push()

fotos_data = {
    "Valencia" : {"name": "massi ", "price": 30},
}

print("Adding")

for slug, foto in fotos_data.items(): 
    new_foto = Foto(slug = slug, name = foto['name'], price = foto['price'])
    db.session.add(new_foto)
    print(new_foto)

db.session.commit()

"""
     GOTTA FIND OUT HOW TO FIX THE SHOP TACHADA Y QUE LLEVE A LOS LINKS DINAMICOS 
"""