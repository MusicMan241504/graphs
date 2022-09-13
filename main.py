import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
with open('data.csv') as file:
    r = csv.reader(file,delimiter=',')
    time = []
    volume1 = []
    volume2 = []
    volume05 = []
    line = 0
    for row in r:
        if line == 0:
            xLabel = row[0]
            v2Label = row[1]
            v1Label = row[2]
            v05Label = row[3]
            line = line + 1
        else:
            time.append(int(row[0]))
            volume2.append(int(row[1]))
            volume1.append(int(row[2]))
            volume05.append(int(row[3]))


time_ = np.linspace(min(time), max(time), 500)

v2spli = make_interp_spline(time, volume2, k=5)
v2_ = v2spli(time_)
v1spli = make_interp_spline(time, volume1, k=5)
v1_ = v1spli(time_)
v05spli = make_interp_spline(time, volume05, k=5)
v05_ = v05spli(time_)


plt.plot(time_, v2_, 'g')
plt.plot(time_, v1_, 'b')
plt.plot(time_, v05_, 'r')
plt.xlabel(xLabel)
plt.ylabel("Volume gas produced /cm^3")
plt.title('Rate of Reaction of Mg and HCl')
plt.legend([v2Label, v1Label, v05Label])
plt.grid()
plt.show()


