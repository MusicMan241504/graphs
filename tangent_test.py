from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15,15,1000)#generate x values
y = np.sin(x)#generate sine curve

x0 = 7.3#x value to create tangent
i0 = np.argmin(np.abs(x-x0))
print(i0)
x1 = x[i0:i0+2]
y1 = y[i0:i0+2]
dydx, = np.diff(y1)/np.diff(x1)#calculate gradient
print(dydx)
tngnt = lambda x: dydx*x + (y1[0]-dydx*x1[0])

plt.plot(x,y)
plt.plot(x1[0],y1[0], "or")
plt.plot(x,tngnt(x), label="tangent")

plt.legend()
plt.show()
