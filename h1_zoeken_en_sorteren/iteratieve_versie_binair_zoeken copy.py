# versie om tijdscomplexiteit te meten


import time                                    # om tijd te meten
import random                                  # om willekeurige zoekitems te kiezen
import numpy as np                             # om snel willekeurige getallen te maken
import matplotlib.pyplot as plt                # om een grafiek te tekenen

def zoek_binair(zoekItem, rij, toon=True):     # toon=True: standaard wél afdrukken (voor de testen)
    n = len(rij)
    l = 0
    r = n - 1
    while l != r:
        if toon:                               # alleen afdrukken als toon True is
            print(f"{l}, {r}")
        m = (l + r) // 2
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
    if rij[l] == zoekItem:
        index = l
    else:
        index = -1
    return index


# experiment tijdscomplexiteit slide 18
if __name__ == "__main__":
    AANTAL_ZOEKITEMS = 30                      # zoals op de slide: 30 willekeurige getallen uit de rij
    HERHALINGEN = 1000                         # elk getal zo vaak zoeken (de slide doet 100 000, maar dat duurt lang)
    list_n = []                                # x-as: de lengtes n
    times = []                                 # y-as: gemiddelde tijd per zoekopdracht

    for k in range(1, 15):                     # n = 2 ... 16384
        n = 2 ** k
        rij = sorted(np.random.randint(0, 100_000_000, size=n).tolist())   # GESORTEERDE rij van n getallen
        zoekitems = random.choices(rij, k=AANTAL_ZOEKITEMS)                # kies 30 getallen die in de rij staan

        totaal = 0.0
        for zoekItem in zoekitems:             # voor elk van de 30 zoekitems ...
            start = time.perf_counter()        # start de klok
            for _ in range(HERHALINGEN):       # ... zoek het 1000 keer
                zoek_binair(zoekItem, rij, toon=False)   # zonder print, anders meten we het afdrukken
            totaal += time.perf_counter() - start        # stop de klok, tel op

        gemiddeld = totaal / (AANTAL_ZOEKITEMS * HERHALINGEN)   # tijd voor ÉÉN zoekopdracht
        list_n.append(n)
        times.append(gemiddeld)
        print(f"n = {n:5d}   gemiddelde tijd = {gemiddeld * 1_000_000:.2f} µs")   # µs = miljoenste seconde

    plt.plot(list_n, times, "o-")
    plt.xlabel("n (lengte van de rij)")
    plt.ylabel("gemiddelde tijd per zoekopdracht (s)")
    plt.title("Binair zoeken: uitvoeringstijd")
    plt.show()