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

    def login(self):
        errors = ''
        if request.method == 'POST':

            login = request.form.get('login')
            if not login:
                errors += 'Login false '

            password = request.form.get('password')
            if not password:
                errors += 'Password false'

            if login and password:
                errors += f'All ok you can login ({login}, {password})'

        return render_template('site/login.html', errors=errors)
