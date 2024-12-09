from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

import webapp.routes.route_index
import webapp.routes.route_historical_traffic
import webapp.routes.route_live_traffic