import imp


import numpy as np

def exp_fade_in(inputwave, attack=1.0, samplerate=44100.0):
    N = len(inputwave)
    t = np.linspace(0, N / samplerate, N)
    fader = 1 - np.exp(- t / attack)
    return inputwave * fader

def exp_fade_out(inputwave, attack=1.0, samplerate=44100.0):
    N = len(inputwave)
    t = np.linspace(0, N / samplerate, N)
    fader = np.exp(- t / attack)
    return inputwave * fader