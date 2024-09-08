from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_jwt_extended import JWTManager
from model import train_model, detect_anomalies
from data_ingestion import data_bp
from auth import auth_bp
from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*")
jwt = JWTManager(app)

app.register_blueprint(data_bp, url_prefix='/data')
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/train', methods=['POST'])
def train():
    train_model()
    return jsonify({"status": "model trained"}), 200

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json['data']
    anomalies = detect_anomalies(data)
    if anomalies:
        for anomaly in anomalies:
            socketio.emit('alert', {'message': f"Anomaly detected: {anomaly}"})
    return jsonify({"anomalies": anomalies}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)