from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd
from database import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from joblib import dump, load
import os

DATABASE_URI = 'postgresql://user:password@localhost:5432/threats'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def load_data():
    query = "SELECT bytes, duration, failed_logins FROM threat_data"
    data = pd.read_sql(query, engine)
    return data

def train_model():
    data = load_data()
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    dump(model, 'model.pkl')
    return model

def detect_anomalies(new_data):
    model = load('model.pkl')
    new_data = np.array(new_data)
    predictions = model.predict(new_data)
    anomalies = new_data[predictions == -1]
    return anomalies.tolist()
