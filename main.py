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
    return WeatherData.query.order_by(WeatherData.id.desc()).first()
    
def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
    return None

def check_weather_conditions(weather_data, get_settings):
    result = {}
    today = datetime.now().date()
    
    min_temp = get_settings.mintemp
    max_temp = get_settings.maxtemp
    max_wind = get_settings.maxwind
    rain_chance = get_settings.rainchance
    snow_chance = get_settings.snowchance
    location = get_settings.city
    
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
    # return {"data":result, "location":WeatherData.query.order_by(WeatherData.id.desc()).first().city,"mintemp":mintemp}

    #         for forecast in weather_data['list']:
    #             forecast_date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
    #             if forecast_date == day:
    #                 temp_k = forecast['main']['temp']
    #                 temp_c = temp_k - 273.15  # Convert from Kelvin to Celsius
    #                 wind_speed = forecast['wind']['speed']
    #                 rain = forecast.get('rain', {}).get('3h', 0)
    #                 snow = forecast.get('snow', {}).get('3h', 0)
                    
    #                 if not (min_temp <= temp_c <= max_temp):
    #                     can_bike = False
    #                 if wind_speed > max_wind:
    #                     can_bike = False
    #                 if rain > rain_chance:
    #                     can_bike = False
    #                 if snow > snow_chance:
    #                     can_bike = False

    #     result[day] = can_bike
    
    # return result
@app.route('/save_settings', methods=['POST'])
def save_settings():
    data = request.get_json()
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
    return jsonify({"id": new_settings.id})

@app.route('/get_settings/<int:id>', methods=['GET'])
def get_settings(id):    
    settings = WeatherData.query.get(id)
    if settings:
        return jsonify({
            "city": settings.city,
            "minTemp": settings.minTemp,
            "maxTemp": settings.maxTemp,
            "maxWind": settings.maxWind,
            "rainChance": settings.rainChance,
            "snowChance": settings.snowChance
        })
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
    settings = get_settings()
    print("Settings:", settings)
    if settings:
        api_key = config.OPENWEATHER_API_KEY
        weather_data = get_weather(city, api_key)
        print("Weather data:", weather_data)
        if weather_data:
            result = check_weather_conditions(weather_data, settings)
            print("Weather conditions:", result)
            return jsonify(result)
        else:
            return jsonify({"error": "Failed to fetch weather data"}), 500
    else:
        return jsonify({"error": "No settings found"}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(port=5000, debug=True)   
 
#dit moet ik gaan loopen dus, voor alle tijden dus 3 uur, 6. 9 uur. 
#volgende stap is: kijken hoe je deze data kan overslaan en voorspelling geven voor de aankomende 3 dagen. 
#na dit werken aan die functie in jsx, om die GET functie werkend te krijgen. 
#die data in de database, moet je eruit kunnen halen en kunnen verantwoorden in de integer. 
#dan beginnen vergelijk functie, 

# dit hieronder is de oude code uitgecomment
# @app.route('/predict/<city>', methods=['GET'])
# @cross_origin("http://localhost:3000")
# def get_weather_prediction(city ):
#     api_key = config.OPENWEATHER_API_KEY
#     url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
#     response = requests.get(url)
#     weather_data = response.json()
    
#     for i in range(20):
        
#         name= weather_data['city']['name']
#         min_temp = weather_data["list"][i]['main']['temp_min']
#         max_temp = weather_data["list"][i]['main']['temp_max']
#         max_wind = weather_data["list"][i]['wind']['speed']
#         rain_chance = weather_data["list"][i].get('rain', {}).get('3h', 0)
#         snow_chance = weather_data["list"][i].get('snow', {}).get('3h', 0)
#         api_weather_data = {"city": name,"mintemp": min_temp,"maxtemp": max_temp, "maxwind": max_wind, "rainchance": rain_chance, "snowchance": snow_chance}
#         return api_weather_data
