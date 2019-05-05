import os
import importlib

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def importController(controller):
    dir = os.scandir('./controllers')
    for elem in dir:
        if os.path.isfile(elem):
            if elem.name.endswith('.py'):
                name = elem.name.replace('.py', '')
                if name == controller:
                    importlib.import_module(f'controllers.{name}')


@app.route('/<page1>')
def route_1(page1):
    importController(page1)
    return f'{page1}'


@app.route('/<page1>/<page2>')
def route_2(page1, page2):
    importController(page1)
    return f'{page1}, {page2}'


# app.debug = True
if __name__ == '__main__':
    app.run()






# from controllers.site import *
# import controllers.site
