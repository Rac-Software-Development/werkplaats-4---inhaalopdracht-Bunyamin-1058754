import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './weatherinput.css';
import Get from './getfunction';

function WeatherInput() {
  const [city, setCity] = useState('');
  const [minTemp, setMinTemp] = useState('');
  const [maxTemp, setMaxTemp] = useState('');
  const [maxWind, setMaxWind] = useState('');
  const [rainChance, setRainChance] = useState('');
  const [snowChance, setSnowChance] = useState('');
  const navigate = useNavigate();

  const handleCityChange = (e) => setCity(e.target.value);
  const handleMinTempChange = (e) => setMinTemp(e.target.value);
  const handleMaxTempChange = (e) => setMaxTemp(e.target.value);
  const handleMaxWindChange = (e) => setMaxWind(e.target.value);
  const handleRainChanceChange = (e) => setRainChance(e.target.value);
  const handleSnowChanceChange = (e) => setSnowChance(e.target.value);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:5000/weather', {
      city: city,
      minTemp: minTemp,
      maxTemp: maxTemp,
      maxWind: maxWind,
      rainChance: rainChance,
      snowChance: snowChance
    })
    .then(response => {
      console.log(response.data);
      navigate(`/predict/${city}`);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };
    // console.log('Entered values:', { city, minTemp, maxTemp, maxWind, rainChance, snowChance });
    return (
      <div className="weather-input-container">
        <h1>Weather Input</h1>
        <div className="form-box">
          <form onSubmit={handleSubmit}>
            <div className="input-group">
              <label>City:</label>
              <input type="text" value={city} onChange={handleCityChange} />
            </div>
            <div className="input-group">
              <label>Min Temperature °C:</label>
              <input type="number" value={minTemp} onChange={handleMinTempChange} />
            </div>
            <div className="input-group">
              <label>Max Temperature °C:</label>
              <input type="number" value={maxTemp} onChange={handleMaxTempChange} />
            </div>
            <div className="input-group">
              <label>Max Wind Speed m/s:</label>
              <input type="number" value={maxWind} onChange={handleMaxWindChange} />
            </div>
            <div className="input-group">
              <label>Rain Chance (%):</label>
              <input type="number" value={rainChance} onChange={handleRainChanceChange} />
            </div>
            <div className="input-group">
              <label>Snow Chance (%):</label>
              <input type="number" value={snowChance} onChange={handleSnowChanceChange} />
            </div>
            <div className="button-group">
              <button type="submit">Predict Bike Weather</button>
            </div>
          </form>
          <Get city={city} />
          <Link to="/" className="link-style">Go Back</Link>
        </div>
      </div>
    );
  }
  
  export default WeatherInput;