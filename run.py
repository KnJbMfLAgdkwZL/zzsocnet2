import os
import importlib

from flask import Flask

#app = Flask(__name__, template_folder='views')
app = Flask(__name__)

'''
from config import Configuration
app.config.from_object(Configuration)
'''

'''
from flask import render_template

@app.route('/')
def index():
    name = 'Zippo'
    return render_template('site/index.html', name=name)


@app.route('/home')
def home():
    return render_template('site/home.html')
'''


def importController(controller):
    dir = os.scandir('./controllers')
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


# app.debug = True
if __name__ == '__main__':
    app.run()

'''

#import controllers.test
#controllers.test.test()
#aa = eval('controllers.test.test')()

#from controllers import test
#test.test()
#aa = eval('test.test')()

#module = __import__('controllers.test')
#instance = module.test.test()
#aa = eval('module.test.test')()

#module = importlib.import_module(f'controllers.test')
#module.test()
#aa = eval('module.test')()



#from controllers.site import *
#site()

#import controllers.site
#controllers.site.site()

'''
