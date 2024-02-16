from .Controller import Controller
from application.models import Products, databaseSession
class HomeController(Controller): 
    def __init__(self) -> None:
        self.name = "this name"
        pass
    
    def index(self):
        products = databaseSession.query(Products).all()
        data = {'title': "homes", "products":products}
        return super().render('index', data)