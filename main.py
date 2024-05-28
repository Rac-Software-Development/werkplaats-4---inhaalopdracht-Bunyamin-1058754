from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
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
    id : Mapped[int]= db.Column(db.Integer, primary_key=True)
    city: Mapped[str] = mapped_column(db.String(100), nullable=False)
    mintemp: Mapped[int] = mapped_column(db.Integer, nullable=False)
    maxtemp: Mapped[int] = mapped_column(db.Integer, nullable=False)
    maxwind: Mapped[int] = mapped_column(db.Integer, nullable=False)
    rainchance: Mapped[int] = mapped_column(db.Integer, nullable=False)
    snowchance: Mapped[int] = mapped_column(db.Integer, nullable=False)

   
with app.app_context():
    db.create_all()


def get_settings():
    conn = SQLAlchemy.connect('bike.db')   
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM settings')
    settings = cursor.fetchall()
    conn.close()
    return settings
    

def get_weather():
    api_key = 'YOUR_API_KEY'
    city = 'YOUR_CITY'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def check_weather_conditions(weather_data, settings):
    result = {}
    can_bike = True
    
    today = datetime.now()
    for i in range(1, 4):
        day = (today + timedelta(days=i)).strftime('%Y-%m-%d')
        can_bike = True
        
        for setting in settings:
            setting_name, min_value, max_value = setting
            
            for forecast in weather_data['list']:
                forecast_date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
                if forecast_date == day:
                    if setting_name == 'temperature':
                        temp_k = forecast['main']['temp']
                        temp_c = temp_k - 273.15  # Convert from Kelvin to Celsius
                        if not (min_value <= temp_c <= max_value):
                            can_bike = False
                    # Voeg meer weercondities toe zoals nodig
                    # ...

        result[day] = can_bike
    
    return result



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
    
    

@app.route('/predict', methods=['GET'])
@cross_origin("http://localhost:3000")
def get_weather_prediction():
    settings = get_settings()
    if settings:
        city = settings[0].city  # Assuming all settings are for the same city
        api_key = config.OPENWEATHER_API_KEY
        weather_data = get_weather(city, api_key)
        result = check_weather_conditions(weather_data, settings)
        return jsonify(result)
    else:
        return jsonify({"error": "No settings found"}), 404
    
if __name__ == '__main__':
    app.run(port=5000)