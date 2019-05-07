from flask import render_template


class test:
    def __init__(self):
        print('Constructor test')

    def __del__(self):
        print('Destructor test')

    def index(self):
        print('index test')
        return render_template('test/index.html')
