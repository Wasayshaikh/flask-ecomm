from flask import Flask
from routers.routes import web,dashboardRoutes
from application.models import create_tables,database_uri
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)


app.secret_key = "123456789"
app.config['SECRET_KEY'] = 'your_secret_key'
create_tables()
# Create a session to interact with the database

csrf = CSRFProtect(app)
app.register_blueprint(web, url_prefix='/')
app.register_blueprint(dashboardRoutes, url_prefix='/dashboard')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404.html'

if __name__ == '__main__':
    
    app.run(debug=True)