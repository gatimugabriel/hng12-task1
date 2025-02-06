from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    response = {
         "email": "geraldg652@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",  
        "github_url": "https://github.com/gatimugabriel/hng12-task1"
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
