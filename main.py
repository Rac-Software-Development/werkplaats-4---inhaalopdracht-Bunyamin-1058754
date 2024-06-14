from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta
import requests
import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/bunya/Desktop/STUDIE/JAAR 1/PERIODE 4/werkplaats-4---inhaalopdracht-Bunyamin-1058754/bike.db"
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    mintemp = db.Column(db.Integer, nullable=False)
    maxtemp = db.Column(db.Integer, nullable=False)
    maxwind = db.Column(db.Integer, nullable=False)
    rainchance = db.Column(db.Integer, nullable=False)
    snowchance = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

def get_settings():
    return WeatherData.query.order_by(WeatherData.id.desc()).first()

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
    return None

def check_weather_conditions(weather_data, settings):
    result = {}
    today = datetime.now().date()
    
    min_temp = settings.mintemp
    max_temp = settings.maxtemp
    max_wind = settings.maxwind
    rain_chance = settings.rainchance
    snow_chance = settings.snowchance
    location = settings.city
    
    for i in range(3):
        day = (today + timedelta(days=i)).strftime('%Y-%m-%d')
        can_bike = True

        day_weather = [forecast for forecast in weather_data['list'] if datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d') == day]
        if not day_weather:
            continue

        for forecast in day_weather:
            temp = day_weather[0]['main']['temp']
            mintemp = day_weather[0]['main']['temp_min']
            maxtemp = forecast['main']['temp_max']
            wind_speed = day_weather[0]['wind']['speed']
            rain = forecast.get('rain', {}).get('3h', 0)
            snow = forecast.get('snow', {}).get('3h', 0)
            
            if int(min_temp) <= int(mintemp) or int(maxtemp) > int(max_temp):
                can_bike = False
            if wind_speed > max_wind:
                can_bike = False
            if rain > rain_chance:
                can_bike = False
            if snow > snow_chance:
                can_bike = False
        
        result[day] = can_bike

    return {"data": result, "location": location, "mintemp": min_temp, "maxtemp": max_temp}

@app.route('/save_settings', methods=['POST'])
def save_settings():
    data = request.get_json()
    print("Received settings data:", data)  # Log de ontvangen settings data
    new_settings = WeatherData(
        city=data['city'], 
        mintemp=data['minTemp'], 
        maxtemp=data['maxTemp'], 
        maxwind=data['maxWind'], 
        rainchance=data['rainChance'], 
        snowchance=data['snowChance']
    )
    
    db.session.add(new_settings)
    db.session.commit()
    print("Saved settings ID:", new_settings.id)  # Log de opgeslagen settings ID
    return jsonify({"id": new_settings.id})

@app.route('/get_settings/<int:id>', methods=['GET'])
def get_settings_route(id):
    print("Fetching settings for ID:", id)  # Log de opgevraagde settings ID
    settings = WeatherData.query.get(id)
    if settings:
        response = {
            "city": settings.city,
            "minTemp": settings.mintemp,
            "maxTemp": settings.maxtemp,
            "maxWind": settings.maxwind,
            "rainChance": settings.rainchance,
            "snowChance": settings.snowchance
        }
        print("Fetched settings:", response)  # Log de opgehaalde settings
        return jsonify(response)
    return jsonify({"error": "No settings found"}), 404

@app.route('/weather', methods=['POST'])
@cross_origin("http://localhost:3000")
def add_weather_data():
    data = request.get_json()
    print("data", data)
    new_weather_data = WeatherData(
        city=data['city'], 
        mintemp=data['minTemp'], 
        maxtemp=data['maxTemp'], 
        maxwind=data['maxWind'], 
        rainchance=data['rainChance'], 
        snowchance=data['snowChance']
    )
    
    db.session.add(new_weather_data)
    db.session.commit()
    return jsonify(data)

@app.route('/predict/<city>', methods=['GET'])
@cross_origin("http://localhost:3000")
def get_weather_prediction(city):
    print(f"Fetching weather prediction for {city}")  # Log de stad waarvoor voorspellingen worden opgehaald
    settings = get_settings()  # Haal de meest recente settings op
    if settings:
        api_key = config.OPENWEATHER_API_KEY
        weather_data = get_weather(city, api_key)
        if weather_data:
            result = check_weather_conditions(weather_data, settings)
            return jsonify(result)
        else:
            return jsonify({"error": "Failed to fetch weather data"}), 500
    else:
        return jsonify({"error": "No settings found"}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(port=5000, debug=True)
