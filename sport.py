from flask import Blueprint
sport_bp = Blueprint('sport', __name__,url_prefix='/sport')

@sport_bp.route('/')
def news():
    return "<p> **** SPORT NEWS ****</p>"

@sport_bp.route('/global')
def news_global():
    return "<p> * SPORT GLOBAL NEWS *</p>"