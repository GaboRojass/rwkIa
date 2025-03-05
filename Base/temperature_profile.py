# temperature_profile.py

def define_temperature_profile():
    """
    Define the ideal temperature profile for lead-free soldering.
    Stages include Ramp-Up, Preheat, Soak, Reflow, and Cool Down.
    """
    profile = {
        "Ramp-Up": "Incremento gradual de temperatura.",
        "Preheat": "Mantener una temperatura estable.",
        "Soak": "Distribución térmica homogénea.",
        "Reflow": "Pico de temperatura (entre 235-250°C).",
        "Cool Down": "Enfriamiento controlado."
    }
    return profile
