from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_time_and_ip():
    timestamp = datetime.utcnow().isoformat() + "Z"
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    return jsonify({
        "timestamp": timestamp,
        "ip": ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)