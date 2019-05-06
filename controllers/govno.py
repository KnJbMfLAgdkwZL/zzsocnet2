from flask import Blueprint
from flask import render_template


xyita = Blueprint('govno', __name__, template_folder='../templates/site')


@xyita.route('/')
def index():
    return render_template('index.html')



