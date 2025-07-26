from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")
OPENROUTER_API_MODEL = os.getenv("OPENROUTER_API_MODEL")

@app.route("/api/smart-summarizer", methods=["POST"])
def smart_summarizer():
    try:
        data = request.get_json()
        data["model"] = OPENROUTER_API_MODEL
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({str(e)}), 500