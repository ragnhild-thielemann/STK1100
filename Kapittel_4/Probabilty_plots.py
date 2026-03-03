
#%%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = []

with open("data.txt","r") as fil:
    for linje in fil:
        verdier = linje.split()
        for v in verdier:
            data.append(float(v))

data.sort()

prosentiler = []
n = len(data)

for i in range(n):
    p = ((i-0.5)/n) #finner prosentilen til det ite elementet i måledataene
    prosentiler.append(p)


z_verdier = [-3,-2.25,-1.32,-1.1,-0.79]

plt.plot(z_verdier,prosentiler[:5],".")
plt.xlabel("Stanariserte verdier for z")
plt.ylabel("Prosentiler fra måledateene")
plt.title("sammenheng mellom prosentiler fra normalfordelingen og reele måledata")
