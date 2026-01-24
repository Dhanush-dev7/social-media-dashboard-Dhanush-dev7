from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Social Media Analytics Dashboard API running"
    })

@app.route("/test")
def test():
    return jsonify({
        "status": "success",
        "message": "API working correctly"
    })

if __name__ == "__main__":
    app.run(debug=True)