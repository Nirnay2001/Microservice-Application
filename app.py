import os

from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder=None)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="healthy")


@app.get("/api/v1/message")
def message():
    return jsonify(message="Hello from the DevOps practice microservice!")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
