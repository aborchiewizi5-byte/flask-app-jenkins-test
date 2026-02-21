from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Jenkins Demo App!", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/add/<a>/<b>")
def add(a, b):
    try:
        result = float(a) + float(b)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
