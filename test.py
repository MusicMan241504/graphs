import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

#create data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([4, 9, 12, 30, 45, 88, 140, 230])

xnew = np.linspace(x.min(), x.max(), 200) 
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(xnew)

#create line chart
plt.plot(xnew,y_smooth)
plt.show()