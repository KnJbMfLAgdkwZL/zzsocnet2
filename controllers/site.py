from flask import render_template
from flask import request


class site:
    def __init__(self):
        print('Constructor site')

    def __del__(self):
        print('Destructor site')

    def index(self):
        print('index site')
        return render_template('site/index.html')

    def home(self):
        print('home site')
        return render_template('site/home.html')

    def page404(self):
        print('home site')
        return render_template('site/page404.html')
