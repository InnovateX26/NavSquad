from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)
locations = []
locations.append({"name":"Main Gate","lat":24.9272,"lon":86.2269})
locations.append({"name":"Security Room","lat":24.9273,"lon":86.2271})
locations.append({"name":"Parking Area","lat":24.9273,"lon":86.2263})
locations.append({"name":"Administrative Block","lat":24.9282,"lon":86.2269})
locations.append({"name":"Principal Office","lat":24.9283,"lon":86.2270})
locations.append({"name":"Examination Cell","lat":24.9283,"lon":86.2268})