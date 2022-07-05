import math
import numpy as np
from scipy.io.wavfile import write

note_names = [
    'C', 'CsDb', 'D', 'DsEb', 'E', 'F', 'FsGb', 'G', 'GsAb', 'A', 'AsBb', 'B' 
]

def write_note(noteid, A4_freq=440, octave=0, duration=1.0, samplerate=44100):
    distance_from_A = noteid - 9
    note_freq = A4_freq * math.pow(2, distance_from_A / 12) * math.pow(2, octave)
    time_array = np.arange(samplerate * duration)
    ft = note_freq * time_array
    sinwave = np.sin(2 * np.pi * ft / samplerate)
    sinwave = np.int16(sinwave * 32767)
    notename = note_names[noteid]
    file_name = f'notes/{notename}{4+octave}inA{A4_freq}.wav'
    write(file_name, samplerate, sinwave)

duration = 0.8
A4_freq = 440
for octave in range(-2, 2):
    for noteid in range(12):
        write_note(noteid, A4_freq, octave, duration) 