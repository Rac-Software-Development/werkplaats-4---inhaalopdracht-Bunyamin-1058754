import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './index.css';
import App from './App';

import WeatherInput from './pages/weatherinput';
import reportWebVitals from './reportWebVitals';
import Get from './pages/getfunction';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route exact path="/" element={<App />} /> {/* Hier is de route voor het startscherm */}
        <Route path="/weatherinput" element={<WeatherInput />} />
        <Route path="/predict/:city" element={<Get />} />
      </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();