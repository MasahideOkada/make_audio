import math
import numpy as np
from scipy.io.wavfile import write
from fader import exp_fade_in, exp_fade_out

note_names = [
    'C', 'CsDb', 'D', 'DsEb', 'E', 'F', 'FsGb', 'G', 'GsAb', 'A', 'AsBb', 'B' 
]

def write_note(noteid, A4_freq=440, octave=0, duration=1.0, samplerate=44100,
               fade_in=True, fade_out=True,
               fade_in_attack=0.1, fade_out_attack=0.07):
    distance_from_A = noteid - 9
    note_freq = A4_freq * math.pow(2, distance_from_A / 12) * math.pow(2, octave)
    time_array = np.arange(samplerate * duration)
    ft = note_freq * time_array
    sinwave = np.sin(2 * np.pi * ft / samplerate)
    if fade_in:
        sinwave = exp_fade_in(sinwave, fade_in_attack)
    if fade_out:
        sinwave = exp_fade_out(sinwave, fade_out_attack)
    sinwave = np.int16(sinwave * 32767)
    notename = note_names[noteid]
    file_name = f'notes/wav/{notename}{4+octave}inA{A4_freq}.wav'
    write(file_name, samplerate, sinwave)

duration = 0.7
A4_freq = 440 
for octave in range(-2, 3):
    for noteid in range(12):
        write_note(noteid, octave=octave, duration=duration)