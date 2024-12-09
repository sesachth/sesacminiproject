from flask import render_template
from webapp import app

@app.route('/')
@app.route('/home')
@app.route('/traffic')
def index():
    return render_template('/index.html', client_id = app.config['NAVER_CLIENT_ID'])