import time
import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(a):
    n = len(a)
    aantal = 0
    for i in range(n - 1):
        for j in range(n - 1, i, -1):          # -1: aftellen!
            aantal += 1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return aantal

# experiment tijdscomplexiteit slide 18
if __name__ == "__main__":
    HERHALINGEN = 3
    list_n = []
    times = []

    for k in range(1, 15):                     # n = 2 ... 16384
        n = 2 ** k                             # n is één getal
        totaal = 0.0
        for _ in range(HERHALINGEN):
            a = np.random.randint(0, 100_000_000, size=n).tolist()
            start = time.perf_counter()        # klok pas starten na het maken van de rij
            bubble_sort(a)
            totaal += time.perf_counter() - start
        list_n.append(n)
        times.append(totaal / HERHALINGEN)     # gemiddelde tijd
        print(f"n = {n:5d}   gemiddelde tijd = {times[-1]:.5f} s")

    plt.plot(list_n, times, "o-")
    plt.xlabel("n (lengte van de rij)")
    plt.ylabel("gemiddelde tijd (s)")
    plt.title("Bubble sort: uitvoeringstijd")
    plt.show()