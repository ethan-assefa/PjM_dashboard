# Create init file for Flask application
###########################################

from flask import Flask

# Initialize a flask class object
app = Flask(__name__)

# Pulls from the routes file 
from app import routes