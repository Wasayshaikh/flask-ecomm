from flask import Blueprint
from application.controllers import home
web = Blueprint('web',__name__)

web.add_url_rule('/',view_func=home.index, methods=['GET'])