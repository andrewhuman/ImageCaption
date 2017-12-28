import numpy as np

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x) :
    return 1.0 - np.tanh(x) ** 2
