import time                                    # om tijd te meten
import numpy as np                             # om snel willekeurige getallen te maken
import matplotlib.pyplot as plt                # om een grafiek te tekenen

def bubble_sort(a):                            # sorteert de lijst a met bubble sort
    n = len(a)                                 # n = aantal elementen in de lijst
    aantal = 0                                 # teller: hoe vaak wordt de if uitgevoerd?
    for i in range(n - 1):                     # ronde i = 0 ... n-2; na ronde i staat plaats i goed
        for j in range(n - 1, i, -1):          # j telt af van n-1 tot i+1 (-1: aftellen!)
            aantal += 1                        # tel elke vergelijking
            if a[j - 1] > a[j]:                # staan de twee buren verkeerd?
                a[j - 1], a[j] = a[j], a[j - 1]    #   ja: wissel ze om
    return aantal                              # geef het aantal vergelijkingen terug

# experiment tijdscomplexiteit slide 18
if __name__ == "__main__":                     # alleen uitvoeren als je dit bestand zelf runt
    HERHALINGEN = 3                            # hoe vaak we elke n testen (om een gemiddelde te nemen)
    list_n = []                                # hier komen alle n-waarden in (x-as van de grafiek)
    times = []                                 # hier komen de gemiddelde tijden in (y-as van de grafiek)

    for k in range(1, 15):                     # k = 1 ... 14, dus n = 2 ... 16384
        n = 2 ** k                             # n = 2 tot de macht k (telkens het dubbele)
        totaal = 0.0                           # totale tijd voor deze n, begint bij 0
        for _ in range(HERHALINGEN):           # herhaal de meting een paar keer (_ = teller die we niet gebruiken)
            a = np.random.randint(0, 100_000_000, size=n).tolist()   # maak n willekeurige getallen, als gewone lijst
            start = time.perf_counter()        # start de klok (pas NA het maken van de rij)
            bubble_sort(a)                     # sorteer de rij: dit is wat we meten
            totaal += time.perf_counter() - start   # stop de klok en tel de tijd van deze meting op
        list_n.append(n)                       # bewaar deze n
        times.append(totaal / HERHALINGEN)     # bewaar de gemiddelde tijd voor deze n
        print(f"n = {n:5d}   gemiddelde tijd = {times[-1]:.5f} s")   # toon n en de tijd ([-1] = laatste element)

    plt.plot(list_n, times, "o-")              # teken de punten (o) en verbind ze met lijnen (-)
    plt.xlabel("n (lengte van de rij)")        # tekst bij de x-as
    plt.ylabel("gemiddelde tijd (s)")          # tekst bij de y-as
    plt.title("Bubble sort: uitvoeringstijd")  # titel van de grafiek
    plt.show()                                 # toon de grafiek in een venster