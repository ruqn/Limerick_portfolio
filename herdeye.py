import matplotlib.pyplot as plt
import csv
import codecs
from math import floor, log
import numpy as np
def detect_bpm(signal: any) -> (float, float):

    # select base two for efficient fourier computation
    lower_base_2 = pow(2, floor(log(len(signal)) / log(2)))
    signal = signal[0:lower_base_2]

    #   doubled sided FFT
    spectrum = np.fft.fft(signal)
    freq = abs(np.fft.fftfreq(len(spectrum)))

    max_index = np.argmax(spectrum)
    breathing_freq = freq[max_index] * 5

    amplitude = (np.abs(spectrum)[max_index]) * 2 / len(spectrum)

    return breathing_freq * 60, amplitude


csvReader = csv.reader(codecs.open('CSVNAME.csv', 'rU', 'utf-16'))

x=[]
yx=[]
yy=[]
yz=[]

with open('CSVNAME.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        yx.append(float(row[0]))
        yy.append(float(row[1]))
        yz.append(float(row[2]))
        #x.append((row[3])
        ##print(row[2])

print(detect_bpm(yx[600:900]))

plt.plot(np.linspace(0,len(yz)-1,len(yz)),yx, marker='.')

plt.title('test')

plt.xlabel('Time')
#plt.ylabel('Acceleration')

plt.show()