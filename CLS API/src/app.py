from flask import Flask, jsonify, render_template
import requests

catbreed_list = []

endpoint = "https://api.thecatapi.com/v1/breeds"
api_key = "fcf58abb-d2e0-4167-b0a6-ef57af37608b"
query_params = {"api_key": api_key}

response = requests.get(endpoint, params=query_params)

#print(response.json())
for item in response.json():
    catbreed_list.append(item["name"])

#print(catbreed_list)
#print(len(catbreed_list))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", breeds=catbreed_list)

if __name__ == '__main__':
    app.run(debug=True)

#print(response.json()[1]["name"])
#print(response.status_code)