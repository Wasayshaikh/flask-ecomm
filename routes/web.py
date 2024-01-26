from flask import Blueprint
from application.controller.HomeController import HomeController 
web = Blueprint('web',__name__)

web.add_url_rule('/',view_func=HomeController.index, methods=['GET'])