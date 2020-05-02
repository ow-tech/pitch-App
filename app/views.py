from flask import render_template
from app import app


#views
@app.route('/')
def index():
    '''
    View root page function that returns the idnex page and its ata

    '''
    return render_tamplate('index.html')