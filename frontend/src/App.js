import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { loadConfig, getConfig } from './utils/config';
import Home from './pages/Home';
import Callback from './pages/Callback';
import Login from './components/Login';

function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initializeConfig = async () => {
      try {
        await loadConfig();
        setLoading(false);
      } catch (error) {
        console.error('Error loading configuration:', error);
      }
    };

    initializeConfig();
  }, []);

  if (loading) {
    return <div>Loading configuration...</div>;
  }

  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/callback" element={<Callback />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
