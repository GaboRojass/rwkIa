# data_visualization.py

# Import necessary libraries for data visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# This module visualizes temperature data in real-time using matplotlib.


def setup_serial(port): 
    """Set up the serial port for reading temperature data."""

    """ 
    Set up the serial port for reading temperature data.
    Returns a Serial object configured with the specified port and settings.
    """

    return serial.Serial(port, 115200, timeout=1)

def visualize_temperature(serial_port): 
    """Visualize temperature data in real-time."""

    """
    Visualize temperature data in real-time.
    Sets up a plot and updates it with data read from the serial port.
    """

    fig, ax = plt.subplots()
    ax.set_ylim(20, 400)  # Temperature range (20 to 400 °C)
    ax.set_title("Real-Time Temperature (6 Thermocouples)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")

    lines = [ax.plot([], [])[0] for _ in range(6)]
    temperaturas = [[] for _ in range(6)]
    tiempo = []

    def update(frame): 
        """Update the plot with new temperature data from the serial port."""

        global tiempo  # Keep track of time for the x-axis

        try:
            data = serial_port.readline().decode().strip()
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

    ani = animation.FuncAnimation(fig, update, interval=1000, blit=True)
    plt.show()
    serial_port.close()
