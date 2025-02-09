# Contains view functions for flask application
###############################################

from flask import render_template
from app import app


## Set-Up Login and Welcome Page ##
# Decorators for the following function
@app.route('/')
@app.route('/userlogin')
def userlogin():
    user = {'user_id':1, 'username': 'Ethan', 'role':'Admin'}

