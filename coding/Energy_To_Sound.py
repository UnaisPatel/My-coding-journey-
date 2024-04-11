import numpy as np
from scipy.io.wavfile import write

# set parameters
duration = 5  # seconds
sampling_freq = 44100  # Hz
tone_freq = 440  # Hz
volume = 0.5  # range [0.0, 1.0]
energy = 2000  # Joule

# calculate amplitude based on energy
amplitude = np.sqrt(energy / (2 * np.pi * sampling_freq))
# generate waveform
time_array = np.arange(duration * sampling_freq)
waveform = amplitude * np.sin(2 * np.pi * tone_freq * time_array / sampling_freq)
# scale waveform with volume
scaled_waveform = volume * waveform / np.max(np.abs(waveform))

# write to audio file
write('output.wav', sampling_freq, scaled_waveform)
