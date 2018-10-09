# -*- coding: UTF-8 -*-
# 3、对生成的信号进行快速傅立叶变换，并显示频谱；
# from scipy.fftpack import fft，fftfreq

import matplotlib.pyplot as plt
import numpy as np

Fs = 1000   # Hz
f1 = 110 # Hz
f2 = 230 # Hz
sample = 1000   # points
ts = 1 / sample # time interval

t = np.arange(sample)   # or
# t = np.linspace(1, sample, sample)
y1 = np.sin(2 * np.pi * f1 * t / Fs)
y2 = np.sin(2 * np.pi * f2 * t / Fs)
y = y1 + 0.5 * y2

# plot the signal
plt.figure(1)
plt.subplot(1, 2, 1)
plt.plot(t, y)
plt.xlabel('time(ms)')
plt.ylabel('amplitude(V)')
plt.title('')

ps = np.abs(np.fft.fft(y)) ** 2
freqs = np.fft.fftfreq(y.size, ts)
idx = np.argsort(freqs)

# plot the signal's spectrum
plt.figure(1)
plt.subplot(1, 2, 2)
fidx = idx[len(idx) // 2:]
plt.plot(freqs[fidx], ps[fidx], 'red')
plt.xlabel('frequency(Hz)')
plt.ylabel('ampliitude(n.d.)')
plt.show()
# close all figures in pylab
# plt.close("all")

