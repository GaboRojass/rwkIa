# Import necessary modules for temperature management and AI model
from temperature_profile import define_temperature_profile

from ai_model import train_model, save_model, load_model, predict_temperature
from flask import Flask, render_template, jsonify
from data_visualization import visualize_temperature
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import random
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Training data for the model
X_train = np.array([[0], [30], [60], [90], [120], [150], [180], [210], [240], [270]]).reshape(-1, 1)
y_train = np.array([25, 80, 120, 150, 180, 220, 245, 250, 230, 200])
model = train_model(X_train, y_train)
save_model(model, "temperature_model.pkl")

# Load the trained model
model = load_model("temperature_model.pkl")


# Training data for the model
X_train = np.array([[0], [30], [60], [90], [120], [150], [180], [210], [240], [270]]).reshape(-1, 1)
y_train = np.array([25, 80, 120, 150, 180, 220, 245, 250, 230, 200])
model = train_model(X_train, y_train)
save_model(model, "temperature_model.pkl")

def predict_temperature(model, time_sec): 
    """Predicts the expected temperature based on the reference profile.""" 
    return model.predict(np.array([[time_sec]]))[0]


def suggest_correction(actual_temp, time_sec): 
    """Suggests temperature corrections based on the ideal profile."""

    """Suggests temperature corrections based on the ideal profile."""
    expected_temp = predict_temperature(model, time_sec)


    diff = actual_temp - expected_temp

    if abs(diff) < 5:
        return "Temperature within expected range."
    elif diff > 5:
        return f"Temperature high. Reduce {diff:.1f}°C gradually."
    else:
        return f"Temperature low. Increase {abs(diff):.1f}°C gradually."

def read_temperature(): 
    """Simulates reading the temperature."""

    """Simulates reading the temperature."""
    return random.uniform(20, 260)  # Simulated temperature reading

def analyze_temperature(temp, t): 
    """Analyzes the temperature and suggests corrections."""

    """Analyzes the temperature and suggests corrections."""
    prediccion = predict_temperature(t)
    diferencia = temp - prediccion
    recomendacion = None

    if abs(diferencia) > 5:  # If the deviation is greater than 5°C, suggest correction
        if diferencia > 0:
            recomendacion = f"Disminuir la temperatura en {abs(diferencia):.1f}°C."
        else:
            recomendacion = f"Aumentar la temperatura en {abs(diferencia):.1f}°C."

    return prediccion, recomendacion

# Example usage of the suggest_correction function

time_now = 100  # Seconds
actual_temp = 160  # Current sensor reading
print(suggest_correction(actual_temp, time_now))

# Serial port configuration for reading temperature data

puerto_serial = serial.Serial('COM3', 115200, timeout=1)

# Graph setup for real-time temperature visualization

fig, ax = plt.subplots()
ax.set_ylim(20, 400)  # Temperature range (20 to 400 °C)
ax.set_title("Real-Time Temperature (6 Thermocouples)")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (°C)")

# Lines for each thermocouple
lines = [ax.plot([], [])[0] for _ in range(6)]
temperaturas = [[] for _ in range(6)]
tiempo = []

def update(frame):
    global tiempo
    try:
        data = puerto_serial.readline().decode().strip()
        if data:
            valores = list(map(float, data.split(",")))
            tiempo.append(len(tiempo))

            for i in range(6):
                temperaturas[i].append(valores[i])
                if len(temperaturas[i]) > 50:
                    temperaturas[i].pop(0)

            for i in range(6):
                lines[i].set_data(range(len(temperaturas[i])), temperaturas[i])

            ax.set_xlim(max(0, len(tiempo) - 50), len(tiempo))

    except:
        pass

    return lines

# Animate the graph to update with new temperature data

ani = animation.FuncAnimation(fig, update, interval=1000, blit=True)
plt.show()

puerto_serial.close()

# Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_temperature')
def get_temperature():
    tiempo_actual = random.randint(0, 270)  # Simulated time in seconds
    temperatura_actual = read_temperature()
    temp_esperada, sugerencia = analyze_temperature(temperatura_actual, tiempo_actual)

    return jsonify({
        'tiempo': tiempo_actual,
        'temperatura_actual': temperatura_actual,
        'temperatura_esperada': temp_esperada,
        'sugerencia': sugerencia
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
