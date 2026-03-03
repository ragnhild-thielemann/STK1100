
## Anslå om et datasett er normalfordelt

#### Definisjon av prosentiler fra reelt datasett
Vi ser på prosentiler av datasettet vi jobber med. Vi ordner de $n$ observasjonene fra minst til størst. Da vil den $i$ te minste observasjonen i listen være **[100  ( $i$ - .5)/n ] ** prosentilen. 

I dette eksempelet tar vi utgangspunkt i datasettet nedenfor, og koden som blir beskrevet er skrevet i [scriptet Probability_plots.py](https://github.com/ragnhild-thielemann/STK1100/blob/main/Kapittel_4/Probability_plots.py)


![ya](https://github.com/ragnhild-thielemann/STK1100/blob/main/images/data.png)

Når vi skal gjøre anslag om dette datasettet er normalfordelt, lager vi først et program som leser datafilen, før alle dataene ordnes i en liste. Dataene i listen blir sortert, før vi finner prosentilene. Datasettet inneholder $n$ = 16 datapunkter, så den første prosentilen vil være 

$$ p = [100 * (1 - 0.5)/16 ] = 0.31 $$ 

Altså vil 3.1% av måledataene være under den 1ste observasjonen. Tilsvarende vil 9.4% av måledataene ha en lavere verdi enn den andre observasjonen osv. 

Vi ønsker å vite om vi kan tilnærme dette med den kummulative fordelingen $cdf$ til normalfordelingen. 

Dette gjøres ved å se i en normalfordelingstabell. Da vi er under 0.5-prosentilen, bruker vi at $\Phi (-z)$ = 1 - $\Phi (z)$ . Dette gir


$$ \Phi (-z) = 1 - \Phi(z) = 0.031 \Leftrightarrow \Phi(z) = 0.969 $$


Av standard normalfordelingstabell ser vi at dette tilsvarer z = 1.89 , slik at prosentilverdien fra normalfordelingstabellen vi er ute etter er -1.89. Dette gjøres for alle verdiene fra de observerte dataene. For det første eksempelet har vi: 

$$ P(-1.89 < z) = \Phi(-1.89) = 0.031 $$

Dette gjøres for alle de observerte verdiene for prosentilene med komandoen 


z_verdier = [norm.ppf(p) for p in prosentiler] 

Dette gir følgene sammenheng mellom z-prosentiler fra normalfordelingtabellen og prosentandelen av målingene som er under den $i$te observasjonen. 

![ya](https://github.com/ragnhild-thielemann/STK1100/blob/main/images/p_riktig.png)



For å finne ut om måledataene våre er tilnærmet normalfordelt, vil det være en linjær sammenheng mellom prosentilene fra normalfordelingen og prosentilene fra måledataene. Derfor plotter vi disse to datasettene mot hverandre, som gir følgene plott

![ya](https://github.com/ragnhild-thielemann/STK1100/blob/main/images/riktig.png)

Da det er en linjær sammenheng mellom z-prosentilene fra normalfordelingstabellen og prosentilene fra måledataene, kan vi konkludere med at de observerte dataene er normalfordelt. 



