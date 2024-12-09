from flask import render_template
from webapp import app

@app.route('/traffic/live')
def traffic_live():
    return render_template('/live_traffic.html')