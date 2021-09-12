from flask import render_template
from . import main
from app import app
@main.app.errorhandler(404)
def four_ow_four(error):
    '''
    Function to render the 404 error page
    ''' 
    return render_template('fourOwfour.html'),404