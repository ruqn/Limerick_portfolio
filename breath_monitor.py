# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:08:03 2019

@author: Cex
"""
import numpy as np
def detect_bpm(signal: any) -> (float, float):
"""
    estimates the breathes per minute of the region using fourier transform and calcuates the amplitude
    of the underlying frequency
    :return: (BPM, amplitude)
    """


# select base two for efficient fourier computation
    lower_base_2 = pow(2, floor(log(len(signal)) / log(2)))
    signal = signal[0:lower_base_2]

# doubled sided FFT
    spectrum = np.fft.fft(signal)
    freq = abs(np.fft.fftfreq(len(spectrum)))

    max_index = np.argmax(spectrum)
    breathing_freq = freq[max_index] * 5

    amplitude = (np.abs(spectrum)[max_index]) * 2 / len(spectrum)

return breathing_freq * 60, amplitude
