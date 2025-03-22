import time
import max31855_simulator

# Definir los pines Chip Select (CS) para cada módulo MAX31855
CS_PINS = [8, 7, 6, 5, 4, 3, 2, 1]  # GPIOs de la Raspberry Pi

# Inicializar los sensores MAX31855
sensors = []
for cs in CS_PINS:
    cs_pin = digitalio.DigitalInOut(getattr(board, f"D{cs}"))
    sensors.append(max31855_simulator.MAX31855(board.SPI(), cs_pin))

# Función para leer temperaturas de todos los sensores
def leer_temperaturas():
    temperaturas = []
    for i, sensor in enumerate(sensors):
        try:
            temp = sensor.temperature
            temperaturas.append(temp)
            print(f"Sensor {i+1}: {temp:.2f} °C")
        except RuntimeError as e:
            print(f"Error al leer Sensor {i+1}: {e}")
    return temperaturas

# Bucle principal
while True:
    leer_temperaturas()
    time.sleep(2)  # Leer cada 2 segundos
