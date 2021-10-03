from flask import Flask, jsonify

app = Flask(__name__)

name_list = ['Abyssinian', 'Aegean']
@app.route("/")
def home():
    return jsonify(name_list)

if __name__ == '__main__':
    app.run()
