import numpy as np
import matplotlib.pyplot as plt

m=np.array([2,3,4,5,6,7])
smoothm=np.arange(2,7.1,0.1)
facets=np.array([6,18,90,1250,57750,94963*2])
vertices=np.array([6,32,370,1066044,347326352,419172756930])

sqr = lambda x: x**2
xlogx = lambda x: x*np.log(x)

plt.plot(m,np.log2(facets),label="Log of number of facets")
plt.plot(m,np.log2(vertices),label="Log of number of vertices")
plt.plot(smoothm,sqr(smoothm), label="m**2")
plt.plot(smoothm,xlogx(smoothm), label="mlogm")
plt.legend()
plt.show()
