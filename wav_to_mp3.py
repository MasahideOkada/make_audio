from email.mime import base
from traceback import format_tb
from pydub import AudioSegment
from glob import glob
import os

for f in glob('notes\\wav\\*.wav'):
    base_name = os.path.basename(f)
    base_name = base_name.split('.')[0]
    mp3_file = f'notes\\mp3\\{base_name}.mp3'
    wav_audio = AudioSegment.from_file(f, format='wav')
    wav_audio.export(mp3_file, format='mp3')