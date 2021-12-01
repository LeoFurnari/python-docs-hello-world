from flask import Flask
from flask import json
app = Flask(__name__)



@app.route('/summary', methods=['GET'])
def summary():
    app.response_class(
        response=json.dumps({"user": "John Doe"}),
        mimetype='application/json'
    )