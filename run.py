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


def load404():
    from controllers.site import site
    return site().page404()


@app.route('/')
@app.route('/<controller>', methods=['GET', 'POST'])
@app.route('/<controller>/', methods=['GET', 'POST'])
def route_1(controller='site'):
    instance = importController(controller)
    if instance:
        method = 'index'
        if hasattr(instance, method):
            return eval(f'instance.{method}')()

    return load404(), 404


@app.route('/<controller>/<method>', methods=['GET', 'POST'])
@app.route('/<controller>/<method>/', methods=['GET', 'POST'])
def route_2(controller='site', method='index'):
    instance = importController(controller)
    if instance:
        if hasattr(instance, method):
            return eval(f'instance.{method}')()

    return load404(), 404


if __name__ == '__main__':
    app.run()
