from flask import render_template, request, redirect, url_for,flash,session
class Controller:
    def __init__(self) -> None:
       pass 
    def render(self,template, data=None):
        if data is None:
            return render_template("pages/"+template + ".html")
        else:
            return render_template("pages/"+template + ".html",**data)
    def request(self):
        return request
    def redirect(self, blue_print):
        return redirect(url_for(blue_print))
    def flash_error(self,error):
        flash(error)
        pass
    def sessions(self, data):
        session
        pass