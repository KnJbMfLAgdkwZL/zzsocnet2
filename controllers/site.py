from flask import render_template
from flask import request


class site:
    def __init__(self):
        print('Constructor site')

    def __del__(self):
        print('Destructor site')

    def index(self):
        print('index site')
        name = 'Zippo'

        name = request.args.get('name')
        
        # return 'Hello From site index'

        return render_template('./site/index.html', name=name)
