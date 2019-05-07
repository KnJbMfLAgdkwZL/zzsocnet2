import os
import importlib

from flask import Flask
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


def importController(controller):
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, 'controllers')
    dir = os.scandir(filepath)
    for elem in dir:
        if os.path.isfile(elem):
            if elem.name.endswith('.py'):
                name = elem.name.replace('.py', '')
                if name == controller:
                    module = importlib.import_module(f'controllers.{name}')
                    instance = eval(f'module.{name}')()
                    return instance
    return False


@app.route('/')
@app.route('/<controller>')
@app.route('/<controller>/')
def route_1(controller='site'):
    html = '404'
    instance = importController(controller)
    if instance:
        method = 'index'
        if hasattr(instance, method):
            html = eval(f'instance.{method}')()
    return html


@app.route('/<controller>/<method>')
@app.route('/<controller>/<method>/')
def route_2(controller='site', method='index'):
    html = '404'
    instance = importController(controller)
    if instance:
        if hasattr(instance, method):
            html = eval(f'instance.{method}')()
    return html


if __name__ == '__main__':
    app.run()
