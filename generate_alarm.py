import numpy as np
from scipy.io.wavfile import write

fs = 44100  # Sample rate
duration = 1  # seconds
frequency = 440  # Hz (A4 tone)

t = np.linspace(0, duration, int(fs*duration), False)
tone = 0.5 * np.sin(2 * np.pi * frequency * t)

audio = (tone * 32767).astype(np.int16)  # Convert to 16-bit PCM
write("alarm.wav", fs, audio)
