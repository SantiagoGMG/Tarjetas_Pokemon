from flask import Flask, jsonify, request , render_template
import requests

app = Flask(__name__)

@app.route("/<id>", methods=['GET'])
def index(id):
    #id = 134
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return render_template("index.html", data = data)
    else:
        print("Fallo la petición")

if __name__ == "__main__":
    #index(100)
    app.run(debug=True, host="0.0.0.0", port=4001)