import numpy as np

def avg_charges(Z):
    TotalCharges = Z['TotalCharges'].values
    Tenure = Z['tenure'].values
    return (TotalCharges / (Tenure + 1e-5)).reshape(-1, 1)