from flask import Blueprint
from application.controllers.HomeController import HomeController 
web = Blueprint('web',__name__)
home = HomeController()
web.add_url_rule('/',view_func=home.index, methods=['GET'])