import json
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

def load_data():
    with open('data.json') as f:
        return json.load(f)

@app.route('/api/info', methods=['GET'])
def get_info():
    data = load_data()
    info = {
        "email": data["email"],
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": data["github_url"]
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)