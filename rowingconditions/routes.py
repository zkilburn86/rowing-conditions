from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    return 'Hello Flask App'