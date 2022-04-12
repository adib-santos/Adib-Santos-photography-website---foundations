from flask import Blueprint, render_template, request, current_app
from . models import Foto

blueprint = Blueprint('fotos', __name__)

current_app.config['POSTS_PER_PAGE']


@blueprint.route('/shop')
def shop():
    page_number = request.args.get('page', 1, type=int)
    fotos_pagination = Foto.query.paginate(page_number, current_app.config['FOTOS_PER_PAGE']) 
    return render_template('shop/index.html', fotos_pagination = fotos_pagination)

@blueprint.route('/shop/<slug>') 
def ind(slug): 
    foto = Foto.query.filter_by(slug=slug).first_or_404()    
    return render_template('/shop/ind.html', foto = foto)
