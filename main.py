from flask import Flask, request, jsonify
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_cors import CORS, cross_origin

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


@app.route('/weather', methods=['POST'])
@cross_origin()
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
    return jsonify({'message': 'new weather data added'})    
    
    
@app.route('/weather', methods=['POST'])
@cross_origin()
def submit():
   
    
 if __name__ == '__main__':
    app.run(port=5000)
