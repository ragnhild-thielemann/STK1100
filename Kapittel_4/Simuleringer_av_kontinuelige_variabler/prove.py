#%%

import numpy as np

import matplotlib.pyplot as plt


def invers(u):
    return (4*u)**(1/2)

f = lambda x: x/2

x_verdier = np.linspace(0,2)

plt.plot(x_verdier,f(x_verdier),label = "F(x) = x/2")
plt.legend()
n = 100000
u_verdier = np.random.uniform(0,1,n)
invers_verdier = invers(u_verdier)
mean = np.sum(invers_verdier)/n
st = np.sum([(k-mean)**2 for k in invers_verdier])/n
plt.ylabel("Tetthet")
plt.xlabel("X = x")
print(np.sqrt(st))
plt.hist(invers_verdier,bins = 50, edgecolor = "black",density = True) #oppretter et histogram, som viser frekvensen til de ulike dataene
#desteny = True - Gjør at vi viser sansynlighetstettheten
plt.show()
print(mean)


