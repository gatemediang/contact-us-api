import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def load_data():
    with open('data.json') as f:
        return json.load(f)

@app.route('/api/info', methods=['GET'])
def get_info():
    data = load_data()
    info = {
        "email": data["email"],
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": data["github_url"],
         # Add version information
    }
    return jsonify(info)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)