from flask import render_template
from webapp import app

@app.route('/')
@app.route('/home')
@app.route('/traffic')
def index():
    return render_template('/index.html')