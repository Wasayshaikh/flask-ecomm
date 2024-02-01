from flask import Flask
from routes.web import web
from application.models import create_session,database_uri
app = Flask(__name__)


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# models.db.init_app(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/blog_post'

session = create_session(database_uri)
# Create a session to interact with the database


app.register_blueprint(web, url_prefix='/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404.html'

#with app.app_context():
    #models.db.create_all()
if __name__ == '__main__':
    
    app.run(debug=True)