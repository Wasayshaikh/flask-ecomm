from flask import Flask
from routes.web import web
from application import models
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/blog_post'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
models.db.init_app(app)

app.register_blueprint(web, url_prefix='/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404.html'

with app.app_context():
    models.db.create_all()
if __name__ == '__main__':
    app.run(debug=True)