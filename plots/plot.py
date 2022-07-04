import numpy as np
import matplotlib.pyplot as plt

m=np.array([2,3,4,5,6])
facets=np.array([6,18,90,1250,57750])

sqr = lambda x: x**2
xlogx = lambda x: x*np.log(x)

plt.plot(m,np.log(facets),label="Log of number of facets")
plt.plot(m,sqr(m), label="m**2")
plt.plot(m,xlogx(m), label="mlogm")
plt.legend()
plt.show()
