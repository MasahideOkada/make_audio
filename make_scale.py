import math
import numpy as np
from scipy.io.wavfile import write
from fader import exp_fade_in, exp_fade_out

scale = [
    0, 2, 4, 5, 7, 9, 11, 12
]

tonic_names = [
    'C', 'CsDb', 'D', 'DsEb', 'E', 'F', 'FsGb', 'G', 'GsAb', 'A', 'AsBb', 'B' 
]

def write_scale(tonic_id, A4_freq=440, octave=0, 
                samplerate=44100, duration=0.5):
    distance_from_A = tonic_id - 9
    tonic_freq = A4_freq * math.pow(2, distance_from_A / 12) * math.pow(2, octave)
    time_array = np.arange(samplerate * duration)
    output = np.array([])
    for s in scale:
        note_freq = tonic_freq * math.pow(2, s / 12)
        ft = note_freq * time_array
        sinwave = np.sin(2 * np.pi * ft / samplerate)
        sinwave = exp_fade_in(sinwave, 0.1)
        sinwave = exp_fade_out(sinwave, 0.07)
        output = np.concatenate([output, sinwave])
    end = np.arange(samplerate * 0.2)
    endwave = np.sin(2 * np.pi * 0 * end / samplerate)
    output = np.concatenate([output, endwave])
    output = np.int16(output * 32767)
    tonic = tonic_names[tonic_id]
    file_name = f'scales/wav/key{tonic}inA{A4_freq}.wav'
    write(file_name, samplerate, output)
    
for tonic_id in range(12):
    write_scale(tonic_id)