
#%%

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
data = []

with open("data.txt","r") as fil:
    for linje in fil:
        verdier = linje.split()
        for v in verdier:
            data.append(float(v))

data.sort()

prosentiler = []
n = len(data)

for i in range(1,n+1):
    p = ((i-0.5)/n) #finner prosentilen til det ite elementet i måledataene
    prosentiler.append(p)


z_verdier = [norm.ppf(p) for p in prosentiler] #finner de tilsvarende prosentilene for dataverdiene
print("z-prosentiler  prosentandel") 

for z, p in zip(z_verdier,prosentiler):
    print(f"{z:8.3f}        {(100*p):6.1f} %")

x_verdier = np.linspace(0.8,1.9,100)
y_verdier = lambda t : -4+ 3*t 


plt.plot(data,z_verdier,".")
plt.ylabel("z_prosentiler")
plt.xlabel("Måledata")
plt.plot(x_verdier,y_verdier(x_verdier), label = "y= 3x -4", color = "hotpink")
plt.legend()
plt.title("sammenheng mellom prosentiler fra normalfordelingen og reele måledata")
plt.show()
