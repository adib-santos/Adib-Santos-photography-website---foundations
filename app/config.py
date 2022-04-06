from dotenv import load_dotenv
from os import environ

load_dotenv()
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

FOTOS_PER_PAGE = 1



# TENGO QUE RECUADRAR MI SHOP Y ARREGLAR 
# MI BASE DE DATOS 