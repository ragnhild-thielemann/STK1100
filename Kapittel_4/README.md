
### Probabilety plots

#### Definisjon av prosentiler fra reelt datasett
Vi ser på prosentiler av datasettet vi jobber med. Vi ordner de $n$ observasjonene fra minst til størst. Da vil den $i$ te minste observasjonen i listen være **[100  ( $i$ - .5)/n ] ** prosentilen. 

I dette eksempelet tar vi utgangspunkt i datasettet nedenfor, og koden som blir beskrevet er skrevet i [scriptet Probability_plots.py](https://github.com/ragnhild-thielemann/STK1100/blob/main/Kapittel_4/Probability_plots.py)


![ya](https://github.com/ragnhild-thielemann/STK1100/blob/main/images/data.png)

Når vi skal gjøre anslag om dette datasettet er normalfordelt, lager vi først et program som leser datafilen, før alle dataene ordnes i en liste. Dataene i listen blir sortert, før vi finner prosentilene. Datasettet inneholder $n$ = 16 datapunkter, så den første prosentilen vil være 

$$ [100 * (1 - 0.5)/16 ] = 0.31 = 3.1 % $$ 

Altså vil 3.1% av måledataene være under den 1ste observasjonen. Tilsvarende vil 9.4% av måledataene ha en lavere verdi enn den andre observasjonen osv. 

Vi ønsker å vite om vi kan tilnærme dette med den kummulative fordelingen $cdf$ til normalfordelingen. 



De ulike prosentilene fra datasettet angir hvor mange prosent av  måledataene som ligger under den gitte verdien. 
Disse prosentilene kan vi plotte mot prosentilene fra standard normalfordeling. Dersom de er linjært fordelt, er det å anta at datasettet vårt er normalfordelt. 

