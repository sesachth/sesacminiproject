from flask import Flask

app = Flask(__name__)

import webapp.routes.route_index
import webapp.routes.route_historical_traffic
import webapp.routes.route_live_traffic