from flask import Blueprint
from application.controllers import home, auth
web = Blueprint('web',__name__)

web.add_url_rule('/',view_func=home.index, methods=['GET'])

#auth Routes
web.add_url_rule('/login',view_func=auth.login, methods=['GET',"POST"])
web.add_url_rule('/register',view_func=auth.register, methods=['GET',"POST"])
web.add_url_rule('/logout',view_func=auth.logout,methods=["GET","POST"])
