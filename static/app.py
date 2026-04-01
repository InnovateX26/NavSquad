rom flask import Flask, render_template, jsonify

app = Flask(__name__)

locations = [
  {"name":"Main Gate","type":"outdoor","description":"Main entrance to GEC Jamui campus","lat":24.9272,"lon":86.2269},
  {"name":"Security Room","type":"room","description":"Campus security post","lat":24.9273,"lon":86.2271},
  {"name":"Parking Area","type":"outdoor","description":"Parking space","lat":24.9273,"lon":86.2263},
  {"name":"Administrative Block","type":"building","description":"Admin building","lat":24.9282,"lon":86.2269},
  {"name":"Principal Office","type":"room","description":"Principal room","lat":24.9283,"lon":86.2270},
  {"name":"Examination Cell","type":"room","description":"Exam office","lat":24.9283,"lon":86.2268},
  {"name":"Accounts Section","type":"room","description":"Fee office","lat":24.9282,"lon":86.2267},
  {"name":"ATM","type":"facility","description":"ATM machine","lat":24.9278,"lon":86.2272},
  {"name":"Academic Block A","type":"building","description":"CSE & IT","lat":24.9290,"lon":86.2260},
  {"name":"CSE Department","type":"room","description":"CSE HOD","lat":24.9290,"lon":86.2259},
  {"name":"IT Department","type":"room","description":"IT Dept","lat":24.9291,"lon":86.2261},
  {"name":"Computer Lab 1","type":"room","description":"Lab 1","lat":24.9291,"lon":86.2259},
  {"name":"Computer Lab 2","type":"room","description":"Lab 2","lat":24.9292,"lon":86.2260},
  {"name":"Academic Block B","type":"building","description":"ECE & EE","lat":24.9290,"lon":86.2275},
  {"name":"ECE Department","type":"room","description":"ECE Dept","lat":24.9290,"lon":86.2275},
  {"name":"EE Department","type":"room","description":"EE Dept","lat":24.9291,"lon":86.2276},
  {"name":"Electronics Lab","type":"room","description":"Electronics Lab","lat":24.9291,"lon":86.2274},
  {"name":"Academic Block C","type":"building","description":"Civil & Mech","lat":24.9295,"lon":86.2268},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/locations")
def get_locations():
    return jsonify(locations)



if __name__ == "__main__":
    app.run(debug=True)