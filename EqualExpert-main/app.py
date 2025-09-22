import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

GITHUB_API = "https://api.github.com"

@app.route("/<username>", methods=["GET"])
def user_gists(username):
    url = f"{GITHUB_API}/users/{username}/gists"
    resp = requests.get(url, timeout=10)

    if resp.status_code == 404:
        return jsonify({"error": "user not found"}), 404
    if resp.status_code != 200:
        return jsonify({"error": "failed to fetch gists"}), 502

    gists = resp.json()
    result = [
        {
            "description": g.get("description"),
            "html_url": g.get("html_url"),
            "id": g.get("id")
        }
        for g in gists
    ]
    return jsonify(result), 200

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Use GET /<username> to fetch public gists."}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
