import random
import time

class MAX31855Simulator:
    def __init__(self, min_temp=20, max_temp=250):
        """Simula un sensor MAX31855 con temperaturas entre min_temp y max_temp."""
        self.min_temp = min_temp
        self.max_temp = max_temp

    def read_temperature(self):
        """Genera una temperatura aleatoria simulando la lectura del MAX31855."""
        temp_celsius = round(random.uniform(self.min_temp, self.max_temp), 2)
        temp_fahrenheit = round((temp_celsius * 9/5) + 32, 2)
        return temp_celsius, temp_fahrenheit

if __name__ == "__main__":
    sensor = MAX31855Simulator()

    print("Simulador de MAX31855 iniciado. Leyendo datos...\n")
    while True:
        temp_c, temp_f = sensor.read_temperature()
        print(f"Temperatura: {temp_c}°C / {temp_f}°F")
        time.sleep(2)  # Simula el tiempo de lectura del sensor (cada 2 segundos)
