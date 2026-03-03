
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

for i in range(n):
    p = ((i-0.5)/n) #finner prosentilen til det ite elementet i måledataene
    prosentiler.append(p)

p_array = np.asarray(prosentiler)

z_prosentiler = norm.cdf(p_array) #finner de tilsvarende prosentilene for dataverdiene
print("z-prosentiler  prosentandel") 

for z, p in zip(z_prosentiler,p_array):
    print(f"{z:.3f}           {p:.3f} %")

#oppretter en graf med heldning 45 grader, for å se om det er en linjær sammenheng mellom prosentilene og måledataene
x_verdier = np.linspace(0,1,100)
y_verdier = lambda x: 0.5 + 0.5*x


plt.plot(p_array,z_prosentiler,".")
plt.ylabel("Stanariserte verdier for z")
plt.xlabel("Prosentiler fra måledateene")
plt.plot(x_verdier,y_verdier(x_verdier), label = "y=x", color = "hotpink")
plt.legend()
plt.title("sammenheng mellom prosentiler fra normalfordelingen og reele måledata")
plt.show()