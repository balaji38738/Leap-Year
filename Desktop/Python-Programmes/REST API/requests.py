from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_data = request.get_json()
        return jsonify({"You sent": user_data})
    else:
        return jsonify({"about": "Hello world"})

@app.route("/square/<int:num>", methods=["GET"])
def square(num):
    return jsonify({"square": num**2})

if __name__ == "__main__":
    app.run(debug=True)

