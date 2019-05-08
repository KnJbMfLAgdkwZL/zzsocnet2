from _core.controller import controller
from flask import render_template


class test(controller):
    def index(self):
        return render_template('test/index.html')
