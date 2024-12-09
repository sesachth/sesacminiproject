from flask import render_template
from webapp import app

@app.route('/traffic/history')
def traffic_history():
    return render_template('/historical_traffic.html')