from .Controller import Controller
from application.helper import check_auth
class DashboardController(Controller): 
    def __init__(self) -> None:
        self.name = "this name"
        pass
    #@check_auth
    def dashboard(self):
        data = {'title': "homes"}
        return self.render('dashboard/home', data)