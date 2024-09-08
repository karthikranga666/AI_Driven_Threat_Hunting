import React, { useState, useEffect } from 'react';
import axios from 'axios';
import OverviewDashboard from './components/OverviewDashboard';
import ThreatMap from './components/ThreatMap';
import AIInsights from './components/AIInsights';
import './App.css';

const App = () => {
  const [threatData, setThreatData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch threat data from backend
  useEffect(() => {
    const fetchThreatData = async () => {
      try {
        const response = await axios.get('/api/threats');
        setThreatData(response.data);
        setIsLoading(false);
      } catch (err) {
        console.error('Error fetching threat data:', err);
        setError(err);
        setIsLoading(false);
      }
    };

    fetchThreatData();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error loading threat data: {error.message}</div>;
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI-Driven Threat Hunting Dashboard</h1>
      </header>

      <main>
        {/* Overview section with charts and summaries */}
        <section className="dashboard-section">
          <OverviewDashboard threatData={threatData} />
        </section>

        {/* Map section visualizing the geographical spread of threats */}
        <section className="map-section">
          <h2>Threat Map</h2>
          <ThreatMap data={threatData} />
        </section>

        {/* AI insights section displaying model-driven insights */}
        <section className="insights-section">
          <h2>AI Insights</h2>
          <AIInsights data={threatData} />
        </section>
      </main>
    </div>
  );
};

export default App;