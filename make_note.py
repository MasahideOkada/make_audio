import math
import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
duration = 1.0
A4_freq = 440
octave = 0
note_freq = A4_freq * math.pow(2, octave)
time_array = np.arange(sample_rate * duration)
ft = np.int64(note_freq * time_array)
sinwave = np.sin(2 * np.pi * ft / sample_rate)
sinwave = np.int16(sinwave * 32767)
file_name = 'notes/A440.wav'
write(file_name, sample_rate, sinwave)