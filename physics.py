import matplotlib.pyplot as plt
import numpy
import scipy

data = numpy.loadtxt('data.csv', delimiter=',')

xdata = data[:,1]
ydata = data[:,0]

plt.scatter(xdata,ydata, marker='x')
slope, intercept, rvalue, pvalue, stderr = scipy.stats.linregress(xdata, ydata)
plt.plot(xdata, [slope * xi + intercept for xi in xdata], color='red')
plt.autoscale()
plt.grid()
plt.title("Light refracting from perspex into air")
plt.xlabel("sinθᵣ")
plt.ylabel("sinθᵢ")
plt.text(0.4,0.15, "gradient = " + str(numpy.round(slope,2)))
plt.show()
