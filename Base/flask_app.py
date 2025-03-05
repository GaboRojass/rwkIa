# flask_app.py

# Import necessary libraries for the Flask application
from flask import Flask, render_template, jsonify

# This module sets up a Flask web application to serve temperature predictions.

from ai_model import load_model, predict_temperature
import random

app = Flask(__name__)

# Load the trained model
model = load_model("temperature_model.pkl")

@app.route('/')
def index(): 
    """Render the main page of the application."""

    return render_template('index.html')

@app.route('/get_temperature')
def get_temperature(): 
    """Return the current and expected temperature as JSON."""

    # Simulate the current time in seconds
    tiempo_actual = random.randint(0, 270)  
    # Simulate a temperature reading

    temperatura_actual = random.uniform(20, 260)  # Simulated temperature reading
    temp_esperada = predict_temperature(model, tiempo_actual)

    # Return the current and expected temperatures in JSON format
    return jsonify({ 

        'tiempo': tiempo_actual,
        'temperatura_actual': temperatura_actual,
        'temperatura_esperada': temp_esperada
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
