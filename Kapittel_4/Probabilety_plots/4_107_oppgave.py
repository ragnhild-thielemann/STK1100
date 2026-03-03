#%%

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

data = []
with open("4_107.txt","r") as fil:
    for linje in fil:
        verdier = linje.split()
        for n in verdier:
            data.append(float(n))


data.sort()
data = np.asarray(data)
prosentiler = []
n = len(data)
print(n)
for i in range(1,n+1):
    p = (i-0.5)/n
    prosentiler.append(p)

prosentiler = np.asarray(prosentiler)
z_verdier = norm.ppf(prosentiler)
#plt.plot(z_verdier,data,".")
#plt.plot(z_verdier,data**2,".",color = "hotpink")
plt.plot(z_verdier,np.sqrt(data),".",color = "skyblue")

print(prosentiler)
print(data)