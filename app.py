from flask import Flask
from routes.web import web
app = Flask(__name__)

app.register_blueprint(web, url_prefix='/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404.html'


if __name__ == '__main__':
    app.run(debug=True)