#%%

import matplotlib.pyplot as plt
import numpy as np


u = np.random.uniform(0,1,100) #gir oss 100000 tilfeldige sansynligehter mellom 0 og 1 (da dette sansynligheten for en gyldig sansynlighet)
l = 3 #lambda
def f(u):
    return np.log(1-u)/-l #den inverse til eksponensialfordelingen

plt.plot(f(u),u,".",label = f"lambda = {l}")
plt.xlabel("Inversfunksjon av eksponensialfordelingen")
plt.ylabel("Uniformt fordelte sansynligehter")
plt.legend()
plt.title ("Invers cdf-metode")
plt.show() #vi plotter sansynlighetene langs y-aksen, og den inverse langs x-aksen. 
#Vi ser av plottet at vi får den kummulative eksponensialfordelignen
