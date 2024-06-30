import os
from flask import Flask

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, '../client/html')

app = Flask(__name__, template_folder=template_dir)

# Define your routes and other configurations

