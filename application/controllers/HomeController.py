from .Controller import Controller
class HomeController(Controller): 
    def __init__(self) -> None:
        self.name = "this name"
        pass
    def index(self):
        data = {'title': "homes"}
        return super().render('pages/index.html', data)