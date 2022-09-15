import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
from scipy import interpolate


def gradient(tck, x):
    dydx = interpolate.splev(x, tck, der=1)
    return dydx


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


v2tck = interpolate.splrep(time, volume2, s=3)
v2_ = interpolate.splev(time_, v2tck, der=0)

v1tck = interpolate.splrep(time, volume1, s=3)
v1_ = interpolate.splev(time_, v1tck, der=0)

v05tck = interpolate.splrep(time, volume05, s=3)
v05_ = interpolate.splev(time_, v05tck, der=0)


v2grad = gradient(v2tck, 0)
v1grad = gradient(v1tck, 0)
v05grad = gradient(v05tck, 0)

'''
concentration = input("Enter the concentration you want to get the gradient of: (2 / 1 / 0.5)")
x = float(input("Enter time value to get gradient at: "))

if concentration == "2":
    grad = gradient(v2tck, x)
    print("Concentration: " + concentration + " Time: " + str(x) + " Gradient: " + str(grad))
elif concentration == "1":
    grad = gradient(v1tck, x)
    print("Concentration: " + concentration + " Time: " + str(x) + " Gradient: " + str(grad))
elif concentration == "0.5":
    grad = gradient(v05tck, x)
    print("Concentration: " + concentration + " Time: " + str(x) + " Gradient: " + str(grad))
'''

plt.plot(time_, v2_, 'g')
plt.plot(time_, v1_, 'b')
plt.plot(time_, v05_, 'r')
plt.xlabel(xLabel)
plt.ylabel("Volume of gas produced /cm\u00b3")
plt.title('Rate of Reaction of Mg and HCl')
text = "Initial rates of reaction:\n"
text = text + "2.00 mol dm\u207b\u00b3: " + str(np.round(v2grad,2)) + " cm\u00b3s\u207b\u00b9\n"
text = text + "1.00 mol dm\u207b\u00b3: " + str(np.round(v1grad,2)) + " cm\u00b3s\u207b\u00b9\n"
text = text + "0.50 mol dm\u207b\u00b3: " + str(np.round(v05grad,2)) + " cm\u00b3s\u207b\u00b9"
plt.text(55,20, text, ha='center', va='center', bbox=dict(boxstyle='round', fc='white', ec='grey'))
plt.legend([v2Label + "\u207b\u00b3", v1Label + "\u207b\u00b3", v05Label + "\u207b\u00b3"])
plt.grid()
plt.savefig("/home/arch/Documents/Coding/Python/graphs/graph.pdf")
plt.show()


