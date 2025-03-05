# ai_model.py

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# This module contains functions for training and using a linear regression model for temperature prediction.


def train_model(X, y):
    """ 
    Train a Linear Regression model with the provided data.
    The model is trained using the input features X and target values y.
    """

    model = LinearRegression()
    model.fit(X, y)
    return model

def save_model(model, filename):
    """
    Save the trained model to a file.
    The model is serialized using pickle and saved to the specified filename.
    """

    with open(filename, "wb") as f:
        pickle.dump(model, f)

def load_model(filename):
    """
    Load a trained model from a file.
    The model is deserialized from the specified filename.
    """

    with open(filename, "rb") as f:
        model = pickle.load(f)
    return model

def predict_temperature(model, time_sec):
    """
    Predict the expected temperature based on the trained model.
    Takes the time in seconds as input and returns the predicted temperature.
    """

    return model.predict(np.array([[time_sec]]))[0]
