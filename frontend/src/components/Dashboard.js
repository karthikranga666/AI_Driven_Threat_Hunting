
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

const Dashboard = () => {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        socket.on('alert', (alert) => {
            setAlerts((prevAlerts) => [...prevAlerts, alert]);
        });
    }, []);

    return (
        <div>
            <h1>Threat Intelligence Dashboard</h1>
            <ul>
                {alerts.map((alert, index) => (
                    <li key={index}>{alert.message}</li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;

