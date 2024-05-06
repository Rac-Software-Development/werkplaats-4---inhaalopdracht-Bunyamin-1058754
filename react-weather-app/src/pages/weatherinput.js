

import react from 'react';
import App from '../App';

import { useState } from 'react';

function WeatherInput() {

    const [city, setCity] = useState('');
    const [minTemp, setMinTemp] = useState('');
    const [maxTemp, setMaxTemp] = useState('');
    const [maxWind, setMaxWind] = useState('');
    const [regenKans, setRegenKans] = useState('');
    const [sneeuwKans, setSneeuwKans] = useState('');

    const handleCityChange = (e) => setCity(e.target.value);
    const handleMinTempChange = (e) => setMinTemp(e.target.value);
    const handleMaxTempChange = (e) => setMaxTemp(e.target.value);
    const handleMaxWindChange = (e) => setMaxWind(e.target.value);
    const handleRegenKansChange = (e) => setRegenKans(e.target.value);
    const handleSneeuwKansChange = (e) => setSneeuwKans(e.target.value);

 // Event handler functie om het formulier in te dienen
 const handleSubmit = (e) => {
    e.preventDefault();
    // Hier kun je de ingevulde waarden verwerken, bijv. naar een API sturen of lokaal opslaan
    console.log('Ingevulde waarden:', { city, minTemp, maxTemp, maxWind, regenKans, sneeuwKans });
    };
    return (
        <form onSubmit={handleSubmit}>
          <label>
            Stad:
            <input type="text" value={city} onChange={handleCityChange} />
          </label>
          <label>
            Minimale temperatuur:
            <input type="number" value={minTemp} onChange={handleMinTempChange} />
          </label>
          <label>
            Maximale temperatuur:
            <input type="number" value={maxTemp} onChange={handleMaxTempChange} />
          </label>
          <label>
            Maximale windsnelheid:
            <input type="number" value={maxWind} onChange={handleMaxWindChange} />
          </label>
          <label>
            Kans op regen (%):
            <input type="number" value={regenKans} onChange={handleRegenKansChange} />
          </label>
          <label>
            Kans op sneeuw (%):
            <input type="number" value={sneeuwKans} onChange={handleSneeuwKansChange} />
          </label>
          <button type="submit">Instellen</button>
        </form>
      );
    }
    
    export default WeatherInput;