import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';
import './weatherinput.css';

function WeatherInput() {
  const [city, setCity] = useState('');
  const [minTemp, setMinTemp] = useState('');
  const [maxTemp, setMaxTemp] = useState('');
  const [maxWind, setMaxWind] = useState('');
  const [rainChance, setRainChance] = useState('');
  const [snowChance, setSnowChance] = useState('');
  const [prediction, setPrediction] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const settingsId = Cookies.get('settingsId');
    if (settingsId) {
      axios.get(`http://127.0.0.1:5000/get_settings/${settingsId}`)
        .then(response => {
          const data = response.data;
          setCity(data.city);
          setMinTemp(data.minTemp);
          setMaxTemp(data.maxTemp);
          setMaxWind(data.maxWind);
          setRainChance(data.rainChance);
          setSnowChance(data.snowChance);
          getPrediction(data);
        })
        .catch(error => {
          console.error('Error fetching settings:', error);
        });
    }
  }, []);

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
      const settingsId = response.data.id;
      Cookies.set('settingsId', settingsId);
      getPrediction({ city, minTemp, maxTemp, maxWind, rainChance, snowChance });
      navigate(`/predict/${city}`);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  const getPrediction = (settings) => {
    axios.post('http://127.0.0.1:5000/predict', settings)
      .then(response => {
        setPrediction(response.data);
      })
      .catch(error => {
        console.error('Error fetching prediction:', error);
      });
  };

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
            <button type="submit">Save to database</button>
          </div>
        </form>
        {prediction && (
          <div>
            <h2>Prediction</h2>
            <p>City: {prediction.location}</p>
            <p>Min Temp: {prediction.mintemp}</p>
            <p>Max Temp: {prediction.maxtemp}</p>
            <p>Prediction for next three days:</p>
            <ul>
              {Object.entries(prediction.data).map(([date, canBike]) => (
                <li key={date}>{date}: {canBike ? 'YES' : 'NO'}</li>
              ))}
            </ul>
          </div>
        )}
        <Link to="/" className="link-style">Go Back</Link>
      </div>
    </div>
  );
}

export default WeatherInput;
