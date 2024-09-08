import React, { useEffect, useState } from 'react';
import socketIOClient from 'socket.io-client';

const ENDPOINT = 'http://localhost:5000';

function Alerts() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const socket = socketIOClient(ENDPOINT);

    // Listen for 'alert' event from the server
    socket.on('alert', (data) => {
      setAlerts((prevAlerts) => [...prevAlerts, data.message]); // Ensure 'data.message' exists
    });

    // Cleanup when component unmounts
    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div>
      <h2>Alerts</h2>
      <ul>
        {alerts.map((alert, index) => (
          <li key={index}>{alert}</li>
        ))}
      </ul>
    </div>
  );
}

export default Alerts;