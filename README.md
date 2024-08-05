# AI_Driven_Threat_Hunting

# AI-Driven Threat Intelligence Platform

An AI-powered platform for threat intelligence that uses anomaly detection to identify potential security threats. This project includes both backend (Flask) and frontend (React) components, all containerized using Docker.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This platform is designed to help organizations identify and analyze potential security threats using machine learning algorithms. The backend is built with Flask, providing a RESTful API, while the frontend is built with React, offering a user-friendly interface.

## Features

- User authentication (register and login)
- Data ingestion for threat analysis
- Machine learning model training
- Anomaly detection based on ingested data
- Dockerized for easy setup and deployment

## Prerequisites

- Git
- Python 3.8+
- Node.js
- Docker and Docker Compose
- An IDE or text editor (e.g., Visual Studio Code)

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-threat-intelligence-platform.git
cd ai-threat-intelligence-platform

```

### Backend Setup

Navigate to the `backend` directory and set up a virtual environment:

```bash

cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt

```

### Frontend Setup

Navigate to the `frontend` directory and install dependencies:

```bash

cd ..\frontend
npm install

```

### Run with Docker Compose

Ensure Docker Desktop is running and start the services:

```bash

cd ..
docker-compose up --build

```

## Usage

### Access the Application

- Backend API: http://localhost:5000
- Frontend: http://localhost:3000

### Register and Login

You can register and log in via the frontend interface or by using tools like Postman to interact with the API directly.

## API Endpoints

### User Authentication

- **Register**: `POST /auth/register`
    - Payload: `{ "username": "your_username", "password": "your_password" }`
- **Login**: `POST /auth/login`
    - Payload: `{ "username": "your_username", "password": "your_password" }`

### Data Ingestion

- **Ingest Data**: `POST /data/ingest`
    - Payload:
        
        ```json
        
        {
          "data": [
            { "feature1": 1.0, "feature2": 3.5 },
            { "feature1": 2.3, "feature2": 1.2 }
          ]
        }
        
        ```
        

### Model Training

- **Train Model**: `POST /train`

### Anomaly Detection

- **Detect Anomalies**: `POST /detect`
    - Payload:
        
        ```json
        
        {
          "data": [
            { "feature1": 1.0, "feature2": 3.5 },
            { "feature1": 2.3, "feature2": 1.2 }
          ]
        }
        
        ```
        

## Contributing

We welcome contributions to this project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear and descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.
