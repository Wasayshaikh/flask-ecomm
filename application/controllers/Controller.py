from flask import render_template, request
class Controller:
    def __init__(self) -> None:
       pass 
    def render(self,template, data):
        return render_template(template,**data)
    def request(self):
        return request