import os
from flask import Flask, jsonify

app = Flask(__name__)

# קוראים את משתני הסביבה מה-ConfigMap וה-Secret
message_from_configmap = os.environ.get('message', 'Hello World!')
api_key_from_secret = os.environ.get('apiKey', 'No API Key Found')

@app.route('/')
def home():
    # נשתמש בהודעה שקראנו מה-ConfigMap
    return message_from_configmap

@app.route('/healthz')
def healthz():
    return jsonify(status="ok")

@app.route('/ready')
def ready():
    return jsonify(status="ready")

@app.route('/info')
def info():
    # דוגמה לשימוש במפתח ה-API
    return jsonify(message=message_from_configmap, api_key=api_key_from_secret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)