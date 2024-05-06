import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './weatherinput.css';

function WeatherInput() {
  const [city, setCity] = useState('');
  const [minTemp, setMinTemp] = useState('');
  const [maxTemp, setMaxTemp] = useState('');
  const [maxWind, setMaxWind] = useState('');
  const [rainChance, setRainChance] = useState('');
  const [snowChance, setSnowChance] = useState('');

  const handleCityChange = (e) => setCity(e.target.value);
  const handleMinTempChange = (e) => setMinTemp(e.target.value);
  const handleMaxTempChange = (e) => setMaxTemp(e.target.value);
  const handleMaxWindChange = (e) => setMaxWind(e.target.value);
  const handleRainChanceChange = (e) => setRainChance(e.target.value);
  const handleSnowChanceChange = (e) => setSnowChance(e.target.value);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Entered values:', { city, minTemp, maxTemp, maxWind, rainChance, snowChance });
  };

  return (
    <div>
      <h1>Weather Input</h1>
      <form onSubmit={handleSubmit}>
        <label>
          City:
          <input type="text" value={city} onChange={handleCityChange} />
        </label>
        <label>
          Min Temperature:
          <input type="number" value={minTemp} onChange={handleMinTempChange} />
        </label>
        <label>
          Max Temperature:
          <input type="number" value={maxTemp} onChange={handleMaxTempChange} />
        </label>
        <label>
          Max Wind Speed:
          <input type="number" value={maxWind} onChange={handleMaxWindChange} />
        </label>
        <label>
          Rain Chance (%):
          <input type="number" value={rainChance} onChange={handleRainChanceChange} />
        </label>
        <label>
          Snow Chance (%):
          <input type="number" value={snowChance} onChange={handleSnowChanceChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
      <br></br>
      <Link to="/" className = "link-style">Go Back</Link>
    </div>
  );
}

export default WeatherInput;
