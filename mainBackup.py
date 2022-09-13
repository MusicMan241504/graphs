import matplotlib.pyplot as plt
import matplotlib
import csv
from scipy.interpolate import make_interp_spline
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



plt.plot(time, volume2, 'o-g')
plt.plot(time, volume1, 'o-b')
plt.plot(time, volume05, 'o-r')
plt.xlabel(xLabel)
plt.ylabel("Volume gas produced /cm^3")
plt.title('Rate of Reaction of Mg and HCl')
plt.legend([v2Label, v1Label, v05Label])
plt.grid()
plt.show()


