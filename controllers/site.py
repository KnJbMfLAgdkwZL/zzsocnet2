from _core.controller import controller
from flask import render_template
from flask import request


class site(controller):
    def index(self):
        return render_template('site/index.html')

    def home(self):
        return render_template('site/home.html')

    def page404(self):
        return render_template('site/page404.html')
