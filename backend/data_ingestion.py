from flask import Blueprint, request, jsonify # type: ignore
from database import db
from datetime import datetime
import logging

data_bp = Blueprint('data', __name__)

class ThreatData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    src_ip = db.Column(db.String(120), nullable=False)
    dst_ip = db.Column(db.String(120), nullable=False)
    src_port = db.Column(db.Integer, nullable=False)
    dst_port = db.Column(db.Integer, nullable=False)
    protocol = db.Column(db.String(10), nullable=False)
    bytes = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    failed_logins = db.Column(db.Integer, nullable=False)

@data_bp.route('/collect', methods=['POST'])
def collect_data():
    data = request.json
    logging.info(f"Data received: {data}")
    threat_data = ThreatData(
        src_ip=data['src_ip'],
        dst_ip=data['dst_ip'],
        src_port=data['src_port'],
        dst_port=data['dst_port'],
        protocol=data['protocol'],
        bytes=data['bytes'],
        duration=data['duration'],
        failed_logins=data['failed_logins']
    )
    db.session.add(threat_data)
    db.session.commit()
    return jsonify({"status": "success"}), 200
