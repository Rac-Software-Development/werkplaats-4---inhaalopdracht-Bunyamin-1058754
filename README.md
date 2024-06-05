### Bike Weather Predictor

## Introduction
This project is a web application that predicts if the weather is good enough to comfortably ride a bike based on the current weather conditions in the city of choice. Users can configure weather settings for example; minimum and maximum temperatures, maximum wind speed, rain chance, snow chance and get predictions for biking conditions in their city.

## Available Scripts
In the project directory, you can run:

### `npm start`
Runs the app in the development mode.
Open http://localhost:3000 to view it in your browser.

The page will reload when you make changes.
You may also see any lint errors in the console.

### npm test
Launches the test runner in the interactive watch mode.
See the section about running tests for more information.

### npm run build
Builds the app for production to the build folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

Your app is ready to be deployed!

See the section about deployment for more information.

### Key Features

1:Weather Configuration: Users can set minimum and maximum temperature, maximum wind speed, rain chance, and snow chance.
2:Weather Prediction: The application fetches weather data and predicts biking conditions for the next three days.
3:Weather Application: This is an extra function that checks the weather normally, like you used to on your mobile device. 

### Requirements
- Python (version 3.12.0) Download Python
- Git (version 2.44.0) Download Git
- Flask
- Virtual environment (venv/virtualenv)

## Installation
To get started with the Flask backend, follow these steps:

1. **Clone the Repository:**
git clone https://github.com/yourusername/bike-indicator.git
cd bike-indicator
2. **Create and Activate a Virtual Environment:**
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
3. **Install Required Packages:**
pip install -r requirements.txt
Run the Flask server:

4. **Run the Flask Server:**
python main.py

## Usage

### Backend (Flask)
The backend is built using Flask and SQLAlchemy. It interacts with the SQLite database to store user configurations and fetches weather data from the OpenWeather API.

- **POST /weather:** Add new weather configuration settings.
- **GET /predict/<city>:** Get weather predictions for the specified city.

### Frontend (React)

- **Weather App:** Users can search for the weather to there liking.
- **Weatherinput:** User can put in there requirements to their liking and save these settings to the database.
- **Result page:** Displays current weather predictions.

## References

- [OpenWeather API](https://openweathermap.org/api)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/)
## AI Assistance

For code formatting and assistance, the following AI tools were used:

- ChatGPT
- GitHub Co-pilot

## Version History

- **Repository Created:** Juli 23, 2023
- **Initial Version Released:** June 4, 2024

## Developer Information

- **Developer:** Bünyamin E. Bölükbas
- **Student Number:** 1058754