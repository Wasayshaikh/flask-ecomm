from flask import render_template
class HomeController:
    def __init__(self) -> None:
        self.name = "this name"
        pass
    def index(self):
        return render_template('pages/index.html', title="home")